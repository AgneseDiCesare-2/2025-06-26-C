from ast import operator

import networkx as nx
from networkx.algorithms.components import connected_components

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo=nx.Graph()
        self._idMap={}

    def get_years(self):
        return DAO.getAllYears()

    def build_graph(self, anno1, anno2):
        self._grafo.clear()
        self._idMap={}
        nodi=DAO.getAllNodi()

        for nodo in nodi:
            self._idMap[nodo.constructorId]=nodo
            tupla=DAO.getAllInfo(nodo.constructorId, anno1, anno2)
            nodo.addinfo(tupla) #aggiorno le informazioni sui piloti

        self._grafo.add_nodes_from(nodi)
        for i in range(len(nodi)):
            for j in range(i + 1, len(nodi)):
                nodo1=nodi[i]
                nodo2=nodi[j]
                #gestisci il caso in cui position sia null x il peso!
                if self.has_connection(nodo1, nodo2):
                    peso=nodo1.completate+nodo2.completate
                    self._grafo.add_edge(nodo1, nodo2, weight=peso)

    def componente_connessa(self):
        connesse=connected_components(self._grafo)
        dizionario=[]

        for g in connesse:
            dizionario.append((g, len(g)))
        ordinato=sorted(dizionario, key=lambda x: x[1], reverse=True)
        return ordinato[0]

    def num_nodi(self):
        return len(self._grafo.nodes)

    def num_archi(self):
        return len(self._grafo.edges)

    def has_connection(self, nodo1, nodo2):
        return len(nodo1.info) > 0 and len(nodo2.info) > 0
        #tanto per cambiare avevo interpretato male
        """anni1=list(nodo1.info.keys())
        anni2=list(nodo2.info.keys())
        for anno in anni1:
            for annot in anni2:
                if anno==annot:
                    return True
        return False"""


