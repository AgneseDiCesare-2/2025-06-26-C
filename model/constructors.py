from dataclasses import dataclass, field


@dataclass
class Constructor:
    constructorId: int
    constructorRef: str
    name: str
    nationality: str
    url: str
    #info={} #{anno: [lista informazioni piloti]
    #completate=0
    info: dict = field(default_factory=dict)  # {anno: [lista informazioni piloti]}
    completate: int = 0

    def addinfo(self, tupla):
        if len(tupla) == 0:
            return

        riga0 = tupla[0]
        self.completate = riga0[4]

        for t in tupla:
            if t[0] in self.info:
                self.info[t[0]].append((t[1], t[2], t[3]))

            else:
                self.info[t[0]] = [(t[1], t[2], t[3])]

    def __hash__(self):
        return hash(self.constructorId)
    def __eq__(self, other):
        return self.constructorId == other.constructorId
    def __str__(self):
        return str(self.name)