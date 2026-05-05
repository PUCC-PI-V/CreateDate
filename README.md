# ViboraInk - Criador de descricoes para tatuagem

Aplicacao desktop em Python com interface feita em `customtkinter` para gerar descricoes de tatuagem com IA, registrar a dificuldade tecnica do trabalho, informar um valor aproximado em reais e salvar tudo em um historico local.

## O que o programa faz

- abre uma interface grafica simples para iniciar o fluxo;
- gera uma descricao de tatuagem usando a API do Gemini;
- permite selecionar a dificuldade tecnica do projeto;
- permite informar o valor aproximado da tatuagem em `R$`;
- salva as informacoes em `tatuagens_geradas.txt`;
- registra o tempo de uso em `tempo_execucao.txt`.

## Estrutura principal

- `main.py`: tela inicial da aplicacao;
- `CreateData.py`: painel principal;
- `getData.py`: janela que conversa com a API do Gemini e salva os dados;
- `.env`: arquivo local com a chave da API;
- `.env.exemple`: modelo de como preencher a variavel de ambiente.

## O que precisa para funcionar

Antes de rodar o projeto, voce precisa de:

- Python instalado;
- acesso a internet;
- uma chave de API do Gemini;
- os pacotes Python usados pelo projeto.

## Dependencias

Opcao recomendada (instalar tudo pelo `requirements.txt`):

```powershell
pip install -r requirements.txt
```

Se quiser usar exatamente o Python do ambiente virtual no Windows:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

Tambem e possivel instalar apenas os pacotes principais manualmente:

Instale estes pacotes no ambiente virtual:

```powershell
pip install customtkinter python-dotenv google-genai
```

Se quiser usar exatamente o Python do ambiente virtual do projeto no Windows:

```powershell
.\venv\Scripts\python.exe -m pip install customtkinter python-dotenv google-genai
```

## Como configurar

### 1. Criar ou ativar o ambiente virtual

Se ainda nao existir um ambiente virtual:

```powershell
python -m venv venv
```

Para ativar no PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Instalar as dependencias

Com o ambiente ativado:

```powershell
pip install -r requirements.txt
```

Se quiser, voce tambem pode instalar apenas os pacotes principais:

```powershell
pip install customtkinter python-dotenv google-genai
```

### 3. Configurar a chave do Gemini

Crie o arquivo `.env` na raiz do projeto com este conteudo:

```env
GEMINI_API_KEY="sua_chave_aqui"
```

Voce tambem pode usar o arquivo `.env.exemple` como referencia.

### 4. Como pegar a chave de API do Gemini (passo a passo)

Se voce ainda nao tem a chave:

1. Acesse o Google AI Studio: [https://aistudio.google.com/](https://aistudio.google.com/);
2. Faça login com sua conta Google;
3. Entre na area de API Keys (normalmente em `Get API key`);
4. Clique em `Create API key`;
5. Copie a chave gerada.

Depois de copiar, substitua no `.env`:

```env
GEMINI_API_KEY="COLE_SUA_CHAVE_REAL_AQUI"
```

Se o projeto ja tiver um `.env` antigo, apenas troque o valor da variavel `GEMINI_API_KEY` pela nova chave.

### 5. Substituindo o `.env` usando o modelo `.env.exemple`

No Windows PowerShell, voce pode copiar o modelo e editar:

```powershell
Copy-Item .env.exemple .env -Force
```

Depois abra o arquivo `.env` e atualize:

```env
GEMINI_API_KEY="SUA_CHAVE_NOVA"
```

Dica: mantenha o `.env` somente no seu computador e nao compartilhe sua chave.

## Como executar

Na raiz do projeto:

```powershell
python main.py
```

Se preferir usar diretamente o Python do ambiente virtual:

```powershell
.\venv\Scripts\python.exe .\main.py
```

## Como usar o programa

1. Abra a aplicacao com `main.py`.
2. Clique em `Iniciar`.
3. No painel principal, clique em `Gerar descricao`.
4. Aguarde a resposta da IA.
5. Leia a descricao gerada.
6. Informe o valor aproximado da tatuagem no campo de valor.
7. Selecione a dificuldade tecnica.
8. Escreva a justificativa.
9. Clique em `Salvar resposta`.

## Explicacao do arquivo `dist/getData.py`

O arquivo `dist/getData.py` e a parte central da janela de geracao de descricao. Em resumo:

- carrega variaveis de ambiente com `load_dotenv()` e le `GEMINI_API_KEY`;
- cria o cliente Gemini com `genai.Client(api_key=API_KEY)`;
- monta a janela `GetData` (interface de resultado, valor, dificuldade e justificativa);
- inicia uma thread (`threading.Thread`) para buscar texto sem travar a interface;
- gera 20 descricoes no metodo `fetch_data()` usando o modelo `gemini-flash-latest`;
- salva as descricoes em `data.txt` para reuso;
- retira uma entrada por vez com `pop_first_entry()` e mostra no campo de resultado;
- persiste a resposta final em `tatuagens_geradas.txt` quando voce clica em `Salvar resposta`.

Se a API estiver indisponivel ou a chave estiver incorreta, esse arquivo mostra mensagens como `Erro ao carregar: ...` no status da tela.

## Gerar executavel com PyInstaller (mais importante)

### Comando solicitado

Use exatamente este comando na raiz do projeto:

```powershell
pyinstaller --onefile --noconsole --name "ViboraInk" --icon ".dist\icon.ico" main.py
```

### Passo a passo completo (Windows + PowerShell)

1. Entre na pasta do projeto:

```powershell
cd C:\CreateDate
```

2. Ative o ambiente virtual (se estiver usando `venv`):

```powershell
.\venv\Scripts\Activate.ps1
```

3. Instale o PyInstaller:

```powershell
pip install pyinstaller
```

4. Execute o build:

```powershell
pyinstaller --onefile --noconsole --name "ViboraInk" --icon ".dist\icon.ico" main.py
```

5. Ao finalizar, o executavel sera criado em:

`dist\ViboraInk.exe`

### Como rodar o executavel

Voce pode iniciar de duas formas:

- pelo Explorer: clique duas vezes em `dist\ViboraInk.exe`;
- pelo PowerShell:

```powershell
.\dist\ViboraInk.exe
```

### Observacoes importantes sobre esse build

- `--onefile`: gera um unico `.exe`;
- `--noconsole`: abre sem janela de terminal;
- `--name "ViboraInk"`: define o nome final do executavel;
- `--icon ".dist\icon.ico"`: define o icone do app (confira se o caminho do icone existe exatamente assim no projeto);
- se o antivirus bloquear na primeira execucao, adicione excecao para a pasta do projeto e teste novamente.

## Arquivos gerados

O programa usa estes arquivos durante a execucao:

- `tatuagens_geradas.txt`: salva descricao, dificuldade, valor e justificativa;
- `tempo_execucao.txt`: registra o tempo total de uso da aplicacao.

## Problemas comuns

### `ModuleNotFoundError`

Significa que alguma dependencia nao foi instalada. Rode:

```powershell
pip install -r requirements.txt
```

Ou, se preferir somente os pacotes principais:

```powershell
pip install customtkinter python-dotenv google-genai
```

### `Erro ao carregar: 404 NOT_FOUND`

Normalmente significa que o nome do modelo Gemini usado no codigo nao existe ou nao esta disponivel para a versao atual da API.

### `Erro ao carregar: 503 UNAVAILABLE`

Significa que a API do Gemini esta temporariamente sobrecarregada. Nesse caso:

- espere alguns segundos e tente novamente;
- teste outro modelo mais leve;
- confira se sua internet esta funcionando normalmente.

### A janela abre, mas a descricao nao aparece

Verifique:

- se o arquivo `.env` existe;
- se `GEMINI_API_KEY` esta preenchida corretamente;
- se a internet esta ativa;
- se a biblioteca `google-genai` esta instalada.

## Observacoes

- o programa depende da API do Gemini para gerar a descricao;
- sem chave valida da API, a geracao nao funciona;
- a interface usa `customtkinter`, entao o `tkinter` precisa estar funcional na sua instalacao do Python;
- o historico e salvo localmente em arquivos `.txt`.
