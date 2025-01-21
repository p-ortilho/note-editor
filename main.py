import sys
from textual.app import App, ComposeResult
from textual.widgets import TextArea, Footer
from textual.binding import Binding
from pathlib import Path



class NoteEditor(App):
    """
    Editor de texto no estilo Vim
    """

    def __init__(self, caminho_arquivo: str | None = None):
        super().__init__()
        self.caminho_arquivo = Path(caminho_arquivo) if caminho_arquivo else None

    # Teclas de atalho
    BINDINGS = [
        Binding('i', 'enter_insert_mode', 'Inserção'),
        Binding('escape', 'exit_mode', 'Leitura'),
        Binding('q', 'quit', 'Sair'),
        Binding('ctrl+s', 'save', 'Salvar')
    ]

    def compose(self) -> ComposeResult:
        """
        Define os widgets da interface.
        """
        texto_inicial:str = ''

        if self.caminho_arquivo and self.caminho_arquivo.exists():
            try:
                texto_inicial = self.caminho_arquivo.read_text()
            except Exception as e:
                self.notify(f'Error ao ler arquivo: {e}')

        yield TextArea(text=texto_inicial, id='editor')
        yield Footer()

    def action_enter_insert_mode(self):
        """
        Ativa o modo de inserção.
        """
        editor = self.query_one('#editor')
        editor.read_only = False  # Permitir edição

    def action_exit_mode(self):
        """
        Retorna ao modo normal.
        """
        editor = self.query_one('#editor')
        editor.read_only = True  # Bloquear edição no modo normal

    def action_save(self):
        """
        Salva o conteúdo editado do arquivo
        """
        if not self.caminho_arquivo:
            self.notify(f'Arquivo não especificado!')
            return

        editor = self.query_one('#editor', TextArea)

        try:
            self.caminho_arquivo.write_text(editor.text)
            self.notify(f'Arquivo salvo com sucesso!')
        except Exception as e:
            self.notify(f'Erro ao salvar arquivo: {e}')


if __name__ == '__main__':
   caminho_arquivo = sys.argv[1]

   if not Path(caminho_arquivo).exists():
       Path(caminho_arquivo).touch()

   app = NoteEditor(caminho_arquivo)
   app.run()