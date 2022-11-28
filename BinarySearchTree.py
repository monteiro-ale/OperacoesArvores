from Node import *


class BinarySearchTree: 
    def __init__(self):
        self.root = None
    
    def insert(self, label):
        #cria um novo no
        node = Node(label) 

        #verifica se árvore está vazia, se sim - nó inserido é raiz
        if self.empty():
            self.root = node
        else: #senao, maos a obra 
            
            #- árvore não vazia - insere recursivamente

            #referencia do nodo pai
            dad_node = None
            current_node = self.root #comeca sempre da raiz

            while True: 

                # Primeira verificacao: currentnode != none (não é folha, nao estavazia) 
                    # -> deve continuar percorrendo 
                if current_node != None: 
                    # e atualizando a referencia do pai
                
                    dad_node = current_node

                    # Segunda Verificacao: verifica se vai para esquerda ou direita
                    if node.getLabel() < current_node.getLabel():
                        #vai para esquerda
                        current_node = current_node.getLeft()
                    else:
                        #vai para direita 
                        current_node = current_node.getRight()
                else:
                    #Terceira verificacao: se current node é none: então encontrou onde deve inserir 

                    #Quarta verificacao: depois de saber que deve inserir
                        # verifica  se vai ser inserido na esquerda ou na direita
                    if node.getLabel() < dad_node.getLabel():
                        dad_node.setLeft(node)
                    else:
                        dad_node.setRight(node)
                    
                    break #insercao realizada

    def empty(self):
        # Raiz vazia: árvore vazia
        if self.root == None:
            return True
        else:
            return False 

    #mostrar árvore - pré-ordem(raiz, esq, dir)
    def show(self, current_node):
        if current_node != None: 
            print('%d' % current_node.getLabel(), end=' ')
            #RECURSIVO
            self.show(current_node.getLeft())
            self.show(current_node.getRight())

    #pega raiz
    def getRoot(self):
        return self.root 

    def search(self, value):
        current = self.root
        while current.getLabel() != value:
            if value < current.getLabel():
                current = current.getLeft()
            else: 
                current = current.getRight()
            if current == None:
                return None
        return current
    
    def delete(self, value):
        if self.root == None:
            print('A arvore está vazia')
            return
        current = self.root
        dad = self.root
        is_left = True
        while current.getLabel() != value:
            dad = current
            #Esquerda
            if value < current.getLabel():
                is_left = True
                current = current.getLeft()
            #Direita
            else: 
                is_left = False
                current = current.getRight()
            if current == None:
                return False
        #Caso nó a ser apagado seja folha
        if current.getLeft() == None and current.getRight() == None:
            if current == self.root:
                self.root = None
            elif is_left == True:
                dad.setLeft(None)
            else: 
                dad.setRight(None)
        # Caso o nó a ser apagado não tenha filho na direita
        elif current.getRight() == None:
            if current == self.root:
                self.root = current.getLeft()
            elif is_left == True:
                dad.setLeft(current.getLeft())
            else:
                dad.setRight(current.getLeft())
        # Caso o nó a ser apagado não tenha filho na esquerda
        elif current.getLeft() == None:
            if current == self.root:
                self.root = current.getRight()
            elif is_left == True:
                dad.setLeft(current.getLeft())
            else:
                dad.setRight(current.getRight())




