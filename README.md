# Envio Automático de E-mails com Anexos

## Descrição

Este script Python permite o envio automatizado de e-mails utilizando a biblioteca `yagmail`. Ele extrai os destinatários de um arquivo Excel (`emails.xlsx`) e envia mensagens personalizadas com um anexo (por padrão, `Curriculo.pdf`).

## Requisitos

Antes de executar o script, certifique-se de que possui:

- **Python 3** instalado
- **Bibliotecas necessárias** (instale com `pip install -r requirements.txt`):
  - `pandas`
  - `yagmail`
  - `keyring`
  - `jinja2`
- **Planilha `emails.xlsx`** preenchida com as colunas:
  - `email`: E-mail do destinatário
  - `nome`: Nome da empresa
  - `cargo`: Cargo para o qual está se candidatando
- **Arquivo `Curriculo.pdf`** ou outro documento a ser anexado
- **Conta Gmail com senha de app configurada** (veja abaixo como configurar)

## Configuração

1. **Configurar senha de app no Gmail**

   - Acesse: [Segurança do Google](https://myaccount.google.com/security)
   - Ative a verificação em duas etapas
   - Gere uma senha de aplicativo e use-a na linha `server.login` do código

2. **Salvar a senha com `keyring`**
   Execute o seguinte comando no terminal substituindo `seu_email@gmail.com` e `sua_senha_do_app`:

   ```bash
   python -c "import keyring; keyring.set_password('smtp', 'seu_email@gmail.com', 'sua_senha_do_app')"
   ```

## Como Usar

1. **Preencha a planilha `emails.xlsx`** com os dados corretos.
2. **Coloque o anexo no diretório do script** (ou altere o caminho no código).
3. **Execute o script**:
   ```bash
   python script.py
   ```

## Estrutura do Código

- **`read_excel_file(file_path)`**: Lê os dados da planilha.
- **`generate_email_body(row)`**: Cria um corpo de e-mail personalizado.
- **`send_email(to, subject, body, attachment, smtp_user, smtp_password, nome)`**: Envia o e-mail com anexo.
- **`main()`**: Função principal que gerencia a execução do script.

## Observações

- Certifique-se de que os arquivos necessários (`emails.xlsx` e `Curriculo.pdf`) estão no mesmo diretório do script.
- O script utiliza `keyring` para armazenar credenciais de forma segura.
- Caso ocorra um erro no envio, verifique se as permissões de segurança do Gmail permitem o uso de aplicativos menos seguros.
- Dica: Se quiser automatizar o envio dos e-mails, pode criar um executável do script (usando pyinstaller) e agendá-lo no Agendador de Tarefas do Windows para rodar no horário desejado. Isso permite enviar os e-mails automaticamente sem precisar executar manualmente o script.

---

**Desenvolvido por:** Richard dos Anjos Oliveira
