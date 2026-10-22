
import sqlite3

from Sala import Sala


class SalaDAO:

    def __init__(self, db_name="salas.db"):

        self.conn = sqlite3.connect(db_name)

        self._criar_tabela()


    def _criar_tabela(self):

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS salas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                bloco TEXT NOT NULL,
                capacidade INTEGER NOT NULL,

                UNIQUE(nome, bloco)
            )
        """)

        self.conn.commit()


    def inserir(self, sala):

        try:

            cur = self.conn.cursor()

            cur.execute("""
                INSERT INTO salas (
                    nome,
                    bloco,
                    capacidade
                )
                VALUES (?, ?, ?)
            """, (
                sala.nome,
                sala.bloco,
                sala.capacidade
            ))

            self.conn.commit()

            sala.id = cur.lastrowid

            return sala

        except sqlite3.IntegrityError as e:

            raise ValueError(
                "Erro ao inserir sala: sala duplicada."
            ) from e


    def buscar_por_id(self, id):

        cur = self.conn.cursor()

        cur.execute("""
            SELECT id, nome, bloco, capacidade
            FROM salas
            WHERE id = ?
        """, (id,))

        row = cur.fetchone()

        if row is None:
            return None

        return Sala(
            id=row[0],
            nome=row[1],
            bloco=row[2],
            capacidade=row[3]
        )


    def buscar_por_nome_bloco(self, nome, bloco):

        cur = self.conn.cursor()

        cur.execute("""
            SELECT id, nome, bloco, capacidade
            FROM salas
            WHERE nome = ? AND bloco = ?
        """, (nome, bloco))

        row = cur.fetchone()

        if row is None:
            return None

        return Sala(
            id=row[0],
            nome=row[1],
            bloco=row[2],
            capacidade=row[3]
        )


    def listar_todos(self):

        cur = self.conn.cursor()

        cur.execute("""
            SELECT id, nome, bloco, capacidade
            FROM salas
        """)

        return [
            Sala(
                id=row[0],
                nome=row[1],
                bloco=row[2],
                capacidade=row[3]
            )
            for row in cur.fetchall()
        ]


    def atualizar(self, sala):

        try:

            cur = self.conn.cursor()

            cur.execute("""
                UPDATE salas

                SET nome = ?,
                    bloco = ?,
                    capacidade = ?

                WHERE id = ?
            """, (
                sala.nome,
                sala.bloco,
                sala.capacidade,
                sala.id
            ))

            self.conn.commit()

            if cur.rowcount == 0:

                raise ValueError(
                    "Sala não encontrada para atualização."
                )

        except sqlite3.IntegrityError as e:

            raise ValueError(
                "Erro ao atualizar sala: sala duplicada."
            ) from e


    def excluir(self, id):

        cur = self.conn.cursor()

        cur.execute("""
            DELETE FROM salas
            WHERE id = ?
        """, (id,))

        self.conn.commit()

        if cur.rowcount == 0:

            raise ValueError(
                "Sala não encontrada para exclusão."
            )


    def fechar(self):

        self.conn.close()
