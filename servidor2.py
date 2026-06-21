"""
API Mock — Painel de Monitoramento de Robôs

Simula a API real usada pelo case técnico de Frontend Jr.
Roda sem dependências externas (só standard library do Python).

Uso:
    python servidor.py

A API fica disponível em http://localhost:8000

Endpoints:
    GET  /robos                        → lista todos os robôs
    GET  /robos/{id}                     → detalhes de um robô
    GET  /robos/{id}/execucoes           → execuções de um robô (últimas 50)
    GET  /execucoes                      → execuções globais (suporta ?status=erro)
    GET  /execucoes/{id}/logs            → logs de uma execução
    GET  /execucoes/{id}/stream          → SSE com logs em tempo real (bônus)
    GET  /status                         → resumo agregado pro dashboard
"""
import json
import random
import time
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


# ─────────────────────── GERAÇÃO DE DADOS FAKE ───────────────────────

ROBOS_TEMPLATE = [
    # Originais (10)
    ("Extrator de Relatórios Bancários", "Baixa relatórios diários dos sistemas bancários"),
    ("Classificador de Documentos", "Classifica PDFs em categorias usando regras"),
    ("Lançamento de Pagamentos", "Lança pagamentos em lote no sistema interno"),
    ("Auditoria de Acessos", "Verifica logs de acesso e gera alertas"),
    ("Sincronizador de Contatos", "Sincroniza contatos entre CRM e e-mail marketing"),
    ("Robô de Boletos", "Emite boletos a partir de planilha"),
    ("Importador de NF-e", "Importa notas fiscais eletrônicas"),
    ("Monitor de Estoque", "Acompanha estoque e dispara alertas de baixa"),
    ("Conciliador Financeiro", "Concilia movimentações bancárias"),
    ("Gerador de Backup", "Faz backup de pastas e envia pro servidor"),
    
    # Novos Robôs — Financeiro & Contábil (10)
    ("Análise de Risco de Crédito", "Consulta bureaus de crédito para novos cadastros de clientes"),
    ("Calculadora de Impostos Retidos", "Valida a retenção de ISS, IRRF e CSLL em notas fiscais"),
    ("Fechamento de Câmbio", "Monitora taxas de câmbio e fecha ordens programadas"),
    ("Disparador de Avisos de Inadimplência", "Envia lembretes automáticos via WhatsApp e E-mail para contas atrasadas"),
    ("Atualização de Índices Inflacionários", "Coleta IGPM e IPCA e atualiza contratos no ERP"),
    ("Rateio de Custos Intervias", "Processa e distribui despesas entre centros de custo"),
    ("Validador de Chaves de Acesso NF-e", "Valida a autenticidade de notas fiscais no portal da SEFAZ"),
    ("Reembolso de Despesas de Viagem", "Lê comprovantes digitais e aprova reembolsos dentro do limite de política"),
    ("Lançamento de Folha de Pagamento", "Exporta dados do sistema de RH e provisiona no ERP financeiro"),
    ("Extrator de Extratos de Cartão de Crédito", "Baixa arquivos EDI das adquirentes para conciliação"),

    # Novos Robôs — Recursos Humanos & Operações (10)
    ("Onboarding de Colaboradores", "Cria contas de e-mail, acessos no Slack e AD para novos funcionários"),
    ("Triagem de Currículos", "Filtra currículos recebidos por palavras-chave de requisitos de vagas"),
    ("Consolidação de Ponto Eletrônico", "Busca marcações de ponto e aponta inconsistências/horas extras"),
    ("Agendador de Exames Periódicos", "Notifica colaboradores sobre vencimento de exames médicos ocupacionais"),
    ("Robô do Clima Organizacional", "Envia pesquisas de Pulse quinzenais e compila resultados anonimizados"),
    ("Distribuidor de Escalas de Plantão", "Gera e publica escalas mensais com base em regras de descanso"),
    ("Gestão de Benefícios VT/VR", "Calcula e solicita recargas de vale transporte e alimentação"),
    ("Offboarding de Colaboradores", "Revoga acessos de funcionários desligados simultaneamente"),
    ("Validador de Certidões de Fornecedores", "Varre sites governamentais para emitir CNDs de parceiros"),
    ("Sincronizador de Metas OKR", "Atualiza o progresso dos times cruzando dados do Jira e do Excel"),

    # Novos Robôs — Comercial, Marketing & CRM (10)
    ("Distribuidor de Leads (Rotativo)", "Direciona novos leads para a equipe comercial seguindo a regra de round-robin"),
    ("Enriquecedor de Dados B2B", "Busca informações corporativas no LinkedIn e Crunchyroll a partir do CNPJ"),
    ("Monitor de Preços de Concorrentes", "Realiza web scraping em e-commerces concorrentes para sugerir precificação"),
    ("Gerador de Propostas Comerciais", "Monta arquivos de proposta personalizados usando dados inseridos no CRM"),
    ("Estatísticas de Campanhas de Anúncios", "Coleta métricas do Meta Ads e Google Ads para relatório unificado"),
    ("Robô de Feedback Pós-Venda", "Dispara pesquisas NPS 7 dias após a entrega dos produtos"),
    ("Renovador Automático de Contratos", "Identifica contratos vencendo em 30 dias e gera minutas de aditivo"),
    ("Sanitizador de Base de E-mails", "Remove e-mails com bounces frequentes ou domínios inválidos"),
    ("Rastreamento de Menções à Marca", "Busca menções no Twitter e portais de notícias para análise de sentimento"),
    ("Atualizador de Catálogo de Marketplace", "Sincroniza o estoque interno com as vitrines da Amazon e Mercado Livre"),

    # Novos Robôs — TI, Infraestrutura & Segurança (10)
    ("Varredura de Vulnerabilidades", "Roda checagens básicas de portas abertas e patches desatualizados nos servidores"),
    ("Sincronizador de Permissões de Pastas", "Ajusta grupos de segurança no Active Directory conforme organograma"),
    ("Purga de Logs Antigos", "Identifica e remove arquivos de log com mais de 90 dias para liberar disco"),
    ("Monitor de Certificados SSL/TLS", "Verifica a validade de todos os domínios da empresa e avisa sobre expiração"),
    ("Alocador de Máquinas Virtuais", "Liga e desliga instâncias de homologação na nuvem para economizar fora do horário comercial"),
    ("Verificador de Integridade de Banco de Dados", "Executa queries de consistência e reporta fragmentação de índices"),
    ("Provisionador de Sandbox", "Monta ambientes temporários para testes automatizados de QA"),
    ("Resetador de Senhas de Autoatendimento", "Desbloqueia contas de usuários que confirmaram identidade via token SMS"),
    ("Análise de Alocação de Licenças SaaS", "Identifica licenças não utilizadas no Microsoft 365 ou Adobe para corte"),
    ("Robô de Deploy de Emergência", "Aplica patches urgentes de segurança em clusters Kubernetes"),

    # Novos Robôs — Logística, Jurídico & Suporte (10)
    ("Rastreamento de Cargas (Correios/Transportadora)", "Atualiza o status de entrega dos pedidos no banco do e-commerce"),
    ("Cotação Automática de Fretes", "Consulta tabelas de 5 transportadoras para achar o menor custo por rota"),
    ("Monitor de Prazos Processuais", "Acompanha diários oficiais em busca de intimações e prazos do time jurídico"),
    ("Extrator de Jurisprudência", "Busca acórdãos em tribunais para embasamento de peças iniciais"),
    ("Triagem de Tickets de Suporte", "Lê chamados recebidos por e-mail e categoriza por nível de criticidade"),
    ("Gerador de Termos de Uso e LGPD", "Atualiza políticas legais nos sites institucionais com base em templates"),
    ("Auditor de Canhotos de Entrega", "Valida se imagens digitalizadas de canhotos possuem assinatura e data"),
    ("Alerta de Quebra de SLA", "Notifica gerentes caso um chamado passe de 80% do tempo limite de resposta"),
    ("Robô de FAQ Automatizado", "Alimenta a base de conhecimento do chatbot com perguntas frequentes dos clientes"),
    ("Agendador de Manutenção de Frota", "Identifica veículos próximos da quilometragem de revisão e agenda na oficina"),
]

NIVEIS = ["INFO", "INFO", "INFO", "INFO", "INFO", "WARNING", "INFO", "INFO", "ERROR", "DEBUG"]

MENSAGENS_INFO = [
    "Robô iniciado",
    "Conectando ao sistema...",
    "Login realizado com sucesso",
    "Buscando registros...",
    "Encontrados {n} registros para processar",
    "Processando registro {n}/{total}...",
    "Salvando resultados...",
    "Robô finalizado com sucesso",
    "Tempo total: {s}s",
    "Cache atualizado",
    "Arquivo {f} baixado",
    "Validação OK",
]

MENSAGENS_WARNING = [
    "Timeout na conexão, tentando novamente",
    "Registro {n} ignorado: campo obrigatório vazio",
    "Conexão lenta detectada",
    "Limite próximo: {x} de {y} requisições usadas",
]

MENSAGENS_ERROR = [
    "Falha de conexão: ConnectionRefused",
    "Erro ao processar registro {n}: KeyError 'documento'",
    "Timeout esgotado após 60s",
    "Arquivo não encontrado: relatorio.xlsx",
    "Credenciais inválidas",
]


def gerar_dados():
    """Gera robôs, execuções e logs fictícios em memória."""
    agora = datetime.now(timezone.utc)
    robos = []
    execucoes = []
    logs_por_execucao = {}

    for i, (nome, descricao) in enumerate(ROBOS_TEMPLATE, start=1):
        robos.append({
            "id": i,
            "nome": nome,
            "descricao": descricao,
            "ativo": random.random() > 0.15,  # ~85% ativos
            "criado_em": (agora - timedelta(days=random.randint(30, 365))).isoformat(),
            "ultima_execucao": None,
            "ultimo_status": None,
        })

    # Aumentado para 1000 execuções para cobrir o volume maior de robôs de forma uniforme nos últimos 14 dias
    exec_id = 1
    for _ in range(1000):
        robo = random.choice(robos)
        if not robo["ativo"]:
            continue

        iniciado = agora - timedelta(
            days=random.randint(0, 13),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
        )
        duracao_s = random.choice([45, 60, 90, 120, 180, 240, 300, 600])
        finalizado = iniciado + timedelta(seconds=duracao_s)

        # 75% sucesso, 15% erro, 5% em andamento, 5% parcial
        r = random.random()
        if r < 0.75:
            status = "sucesso"
        elif r < 0.90:
            status = "erro"
        elif r < 0.95:
            status = "em_andamento"
            finalizado = None
        else:
            status = "parcial"

        exec_data = {
            "id": exec_id,
            "robo_id": robo["id"],
            "iniciado_em": iniciado.isoformat(),
            "finalizado_em": finalizado.isoformat() if finalizado else None,
            "status": status,
            "duracao_segundos": duracao_s if finalizado else None,
        }
        execucoes.append(exec_data)

        # Gera logs pra essa execução
        n_logs = random.randint(8, 40)
        logs = []
        ts = iniciado
        for j in range(n_logs):
            nivel = random.choice(NIVEIS)
            if nivel == "ERROR":
                msg = random.choice(MENSAGENS_ERROR)
            elif nivel == "WARNING":
                msg = random.choice(MENSAGENS_WARNING)
            else:
                msg = random.choice(MENSAGENS_INFO)
            msg = (msg
                   .replace("{n}", str(random.randint(1, 100)))
                   .replace("{total}", str(random.randint(100, 1000)))
                   .replace("{s}", str(duracao_s))
                   .replace("{x}", str(random.randint(800, 950)))
                   .replace("{y}", "1000")
                   .replace("{f}", random.choice(["relatorio.xlsx", "dados.csv", "notas.zip"])))
            logs.append({
                "id": len(logs) + 1,
                "nivel": nivel,
                "mensagem": msg,
                "criado_em": ts.isoformat(),
            })
            ts += timedelta(seconds=duracao_s / n_logs)

        logs_por_execucao[exec_id] = logs
        exec_id += 1

    # Ordena execuções por data
    execucoes.sort(key=lambda e: e["iniciado_em"], reverse=True)

    # Preenche última execução em cada robô
    for r in robos:
        execs_do_robo = [e for e in execucoes if e["robo_id"] == r["id"]]
        if execs_do_robo:
            ultima = execs_do_robo[0]
            r["ultima_execucao"] = ultima["iniciado_em"]
            r["ultimo_status"] = ultima["status"]

    return robos, execucoes, logs_por_execucao


# Carrega dados na inicialização
ROBOS, EXECUCOES, LOGS = gerar_dados()
print(f"✓ Dados fake gerados: {len(ROBOS)} robôs, {len(EXECUCOES)} execuções, "
      f"{sum(len(v) for v in LOGS.values())} logs")


# ─────────────────────── HTTP HANDLER ───────────────────────

class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Log mais limpo
        print(f"  {self.command} {self.path} → {args[1] if len(args) > 1 else '?'}")

    def _send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        # CORS — permite o frontend acessar de outra porta (dev server, etc.)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(body)

    def _send_404(self, msg="Não encontrado"):
        self._send_json({"detail": msg}, status=404)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        qs = parse_qs(parsed.query)

        # ─── GET /status ───
        if path == "/status":
            agora = datetime.now(timezone.utc)
            ultimas_24h = [e for e in EXECUCOES
                           if (agora - datetime.fromisoformat(e["iniciado_em"])).total_seconds() < 86400]
            self._send_json({
                "total_robos_ativos": sum(1 for r in ROBOS if r["ativo"]),
                "robos_em_execucao_agora": sum(1 for e in EXECUCOES if e["status"] == "em_andamento"),
                "execucoes_24h": len(ultimas_24h),
                "falhas_24h": sum(1 for e in ultimas_24h if e["status"] == "erro"),
            })
            return

        # ─── GET /robos ───
        if path == "/robos":
            self._send_json(ROBOS)
            return

        # ─── GET /robos/{id} ───
        if path.startswith("/robos/") and "/execucoes" not in path:
            try:
                robo_id = int(path.split("/")[2])
            except (ValueError, IndexError):
                self._send_404("ID de robô inválido")
                return
            robo = next((r for r in ROBOS if r["id"] == robo_id), None)
            if not robo:
                self._send_404("Robô não encontrado")
                return
            self._send_json(robo)
            return

        # ─── GET /robos/{id}/execucoes ───
        if path.startswith("/robos/") and path.endswith("/execucoes"):
            try:
                robo_id = int(path.split("/")[2])
            except (ValueError, IndexError):
                self._send_404("ID de robô inválido")
                return
            execs = [e for e in EXECUCOES if e["robo_id"] == robo_id][:50]
            self._send_json(execs)
            return

        # ─── GET /execucoes ───
        if path == "/execucoes":
            status_filtro = qs.get("status", [None])[0]
            limite = int(qs.get("limit", ["100"])[0])
            execs = EXECUCOES
            if status_filtro:
                execs = [e for e in execs if e["status"] == status_filtro]
            self._send_json(execs[:limite])
            return

        # ─── GET /execucoes/{id}/logs ───
        if path.startswith("/execucoes/") and path.endswith("/logs"):
            try:
                exec_id = int(path.split("/")[2])
            except (ValueError, IndexError):
                self._send_404("ID de execução inválido")
                return
            logs = LOGS.get(exec_id, [])
            self._send_json(logs)
            return

        # ─── GET /execucoes/{id}/stream — SSE (bônus) ───
        if path.startswith("/execucoes/") and path.endswith("/stream"):
            try:
                exec_id = int(path.split("/")[2])
            except (ValueError, IndexError):
                self._send_404("ID inválido")
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Connection", "keep-alive")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            # Emite 10 logs fake, um por segundo
            try:
                for i in range(10):
                    nivel = random.choice(NIVEIS)
                    msg = random.choice(MENSAGENS_INFO).replace("{n}", str(i))
                    log = {
                        "id": 9999 + i,
                        "nivel": nivel,
                        "mensagem": f"[stream] {msg}",
                        "criado_em": datetime.now(timezone.utc).isoformat(),
                    }
                    payload = f"data: {json.dumps(log, ensure_ascii=False)}\n\n"
                    self.wfile.write(payload.encode("utf-8"))
                    self.wfile.flush()
                    time.sleep(1)
            except (BrokenPipeError, ConnectionResetError):
                pass
            return

        self._send_404()


# ─────────────────────── MAIN ───────────────────────

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("\n╔══════════════════════════════════════════════════╗")
    print("║   API Mock — Painel de Monitoramento de Robôs    ║")
    print("║                                                  ║")
    print("║   Rodando em: http://localhost:8000               ║")
    print("║                                                  ║")
    print("║   Endpoints:                                     ║")
    print("║      GET /status                                 ║")
    print("║      GET /robos                                  ║")
    print("║      GET /robos/{id}                             ║")
    print("║      GET /robos/{id}/execucoes                   ║")
    print("║      GET /execucoes  (?status=erro)              ║")
    print("║      GET /execucoes/{id}/logs                    ║")
    print("║      GET /execucoes/{id}/stream  (SSE — bônus)   ║")
    print("║                                                  ║")
    print("║   Ctrl+C pra parar                               ║")
    print("╚════════════════════════════════════════════════════╝\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n✓ Servidor encerrado.")