import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._anno2 = None
        self._anno1 = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleBuildGraph(self, e):
        if self._anno1 is None or self._anno1 == "" or self._anno2 is None or self._anno2 == "" :
            self._view._txtGraphDetails.controls.append(ft.Text("Seleziona gli anni per continuare!", color="red"))
            self._view.update_page()
            return
        self._model.build_graph(self._anno1, self._anno2)
        self._view._txtGraphDetails.controls.append(ft.Text(f"Grafo creato! Ha {self._model.num_nodi()} nodi e {self._model.num_archi()} archi. "))
        self._view.update_page()
        return

    def handlePrintDetails(self, e):
        m=self._model.componente_connessa() #dizionario
        for i in m.keys():
            self._view._txtGraphDetails.controls.append(ft.Text(f"{i[0].name} --> {m[i]}"))
        self._view.update_page()


    def handleCercaTeamSfortunati(self, e):
        pass

    def fill_DDYear1(self):
        self._view._ddYear1.options.clear()
        anni = self._model.get_years()
        for n in anni:
            self._view._ddYear1.options.append(
                ft.dropdown.Option(key=n, data=n, on_click=self.getAnno1)
            )
        self._view.update_page()
        pass

    #riempio i dropdown
    def getAnno1(self, e):
        selected_key = e.control.data
        self._anno1 = selected_key
        return

    def fill_DDYear2(self):
        self._view._ddYear2.options.clear()
        anni = self._model.get_years()
        for n in anni:
            self._view._ddYear2.options.append(
                ft.dropdown.Option(key=n, data=n, on_click=self.getAnno2)
            )
        self._view.update_page()
        pass

    def getAnno2(self, e):
        selected_key = e.control.data
        self._anno2 = selected_key
        return