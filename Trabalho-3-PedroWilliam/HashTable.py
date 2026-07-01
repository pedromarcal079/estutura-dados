"""
Módulo: HashTable.py
Implementação de Tabelas Hash com tratamentos de colisão avançados.
"""

# ==============================================================================
# 1. TABELA HASH COM ENDEREÇAMENTO LIVRE (SONDAGEM LINEAR)
# ==============================================================================
class HashTableEnderecamentoLivre:
    def __init__(self, capacidade=15000):
        # Usamos None para slots vazios. Guardamos [chave, valor] ou um marcador de "deletado"
        self.tabela = [None] * capacidade
        self.capacidade = capacidade
        self.DELETADO = "__DELETADO__"

    def _hash(self, chave):
        return hash(chave) % self.capacidade

    def adicionar(self, chave, valor):
        indice = self._hash(chave)
        primeiro_deletado = None
        
        # Sondagem linear procurando a chave ou um espaço livre
        for i in range(self.capacidade):
            idx_atual = (indice + i) % self.capacidade
            slot = self.tabela[idx_atual]
            
            if slot is None:
                # Se achou espaço vazio, usa o primeiro slot deletado para otimizar se houver
                alocar_em = primeiro_deletado if primeiro_deletado is not None else idx_atual
                self.tabela[alocar_em] = [chave, valor]
                return True
                
            if slot == self.DELETADO:
                if primeiro_deletado is None:
                    primeiro_deletado = idx_atual
                continue
                
            if slot[0] == chave:
                # Chave encontrada: atualiza o valor
                slot[1] = valor
                return True
                
        return False # Tabela cheia

    def buscar(self, chave):
        indice = self._hash(chave)
        
        for i in range(self.capacidade):
            idx_atual = (indice + i) % self.capacidade
            slot = self.tabela[idx_atual]
            
            if slot is None:
                return None # Parada precoce: se estivesse aqui, a sondagem teria ocupado este slot
            if slot == self.DELETADO:
                continue
            if slot[0] == chave:
                return slot[1]
                
        return None

    def remover(self, chave):
        indice = self._hash(chave)
        
        for i in range(self.capacidade):
            idx_atual = (indice + i) % self.capacidade
            slot = self.tabela[idx_atual]
            
            if slot is None:
                return False
            if slot == self.DELETADO:
                continue
            if slot[0] == chave:
                # Coloca a flag DELETADO para não quebrar futuras buscas da sondagem
                self.tabela[idx_atual] = self.DELETADO
                return True
                
        return False


# ==============================================================================
# 2. TABELA HASH COM ENCADEAMENTO POR ÁRVORE BINÁRIA DE BUSCA (BST)
# ==============================================================================
class NoBST:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.esquerdo = None
        self.direito = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, valor):
        self.raiz = self._inserir_recursivo(self.raiz, chave, valor)

    def _inserir_recursivo(self, no, chave, valor):
        if no is None:
            return NoBST(chave, valor)
        
        if chave == no.chave:
            no.valor = valor # Atualiza
        elif chave < no.chave:
            no.esquerdo = self._inserir_recursivo(no.esquerdo, chave, valor)
        else:
            no.direito = self._inserir_recursivo(no.direito, chave, valor)
        return no

    def buscar(self, chave):
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, no, chave):
        if no is None or no.chave == chave:
            return no.valor if no else None
        if chave < no.chave:
            return self._buscar_recursivo(no.esquerdo, chave)
        return self._buscar_recursivo(no.direito, chave)

    def remover(self, chave):
        self.raiz, deletado = self._remover_recursivo(self.raiz, chave)
        return deletado

    def _remover_recursivo(self, no, chave):
        if no is None:
            return no, False
        
        deletado = False
        if chave < no.chave:
            no.esquerdo, deletado = self._remover_recursivo(no.esquerdo, chave)
        elif chave > no.chave:
            no.direito, deletado = self._remover_recursivo(no.direito, chave)
        else:
            # Encontrou o nó a ser removido
            deletado = True
            if no.esquerdo is None:
                return no.direito, deletado
            elif no.direito is None:
                return no.esquerdo, deletado
            
            # Nó com dois filhos: busca o sucessor in-order (menor na subárvore direita)
            sucessor = self._min_valor_no(no.direito)
            no.chave = sucessor.chave
            no.valor = sucessor.valor
            no.direito, _ = self._remover_recursivo(no.direito, sucessor.chave)
            
        return no, deletado

    def _min_valor_no(self, no):
        atual = no
        while atual.esquerdo is not None:
            atual = atual.esquerdo
        return atual


class HashTableEncadeamentoArvore:
    def __init__(self, capacidade=1000):
        # Cada slot inicializa com uma instância independente de Árvore Binária
        self.tabela = [ArvoreBinariaBusca() for _ in range(capacidade)]
        self.capacidade = capacity_placeholder = capacidade

    def _hash(self, chave):
        return hash(chave) % self.capacidade

    def adicionar(self, chave, valor):
        indice = self._hash(chave)
        self.tabela[indice].inserir(chave, valor)

    def buscar(self, chave):
        indice = self._hash(chave)
        return self.tabela[indice].buscar(chave)

    def remover(self, chave):
        indice = self._hash(chave)
        return self.tabela[indice].remover(chave)