# ✏️NoteEditor

## 📝Descrição

O NoteEditor é um editor de texto simples inspirado no estilo de operação do Vim, desenvolvido utilizando o framework Textual. Ele vem com funcionalidades básicas de leitura, edição e salvamento de arquivos de texto diretamente no terminal.

## ⭐Funcionalidades Principais

### 🔄Modos de Edição:
- Modo de Inserção: Permite editar o conteúdo do arquivo.
- Modo de Leitura: Bloqueia edição, permitindo apenas navegação.

## ⌨️Atalhos do Teclado:
- `i`: Entrar no modo de inserção.
- `esc`: Voltar para o modo de leitura.
- `q`: Sair do aplicativo.
- `Ctrl+S`: Salvar o arquivo

Compatível com arquivos existentes e permite criar novos arquivos se o caminho fornecido não existir.

## ⚠️Limitações
Este editor é minimalista e, atualmente, suporta apenas edições básicas de arquivos de texto. Funcionalidades avançadas encontradas em editores como o Vim podem ser adicionadas futuramente.

## 🚀Instalação 

1. Clone ou baixe este repositório.
2. Instale as dependências com o comando:
~~~
pip install - r requirements.txt
~~~
3. Abra um arquivo existente para editar:
~~~
python main.py <caminho para o arquivo>
~~~
## 🔰 Como Usar 🔰
- Entre no modo de edição pressionando `i` e faça as alterações necessárias. Para salvar as mudanças, pressione `Ctrl+S`.
Pressione `esc` para retornar ao modo de leitura, e `q` para sair do aplicativo.