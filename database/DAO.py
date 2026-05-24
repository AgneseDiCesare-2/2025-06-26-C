from database.DB_connect import DBConnect
from model.constructors import Constructor


class DAO():
    @staticmethod
    def getAllConstructors():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                    from constructors"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllYears():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct r.`year` 
                    from races r
                    order by r.`year` DESC"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["year"]) #lista di anni

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllNodi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct c.constructorId, c.constructorRef, c.name, c.nationality, c.url 
                    from results r, constructors c 
                    where r.constructorId = c.constructorId """
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Constructor(**row)) #lista di Constructor

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllInfo(constructorId, anno1, anno2):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ select tab1.`year`, tab1.driverId, tab1.`position`, tab1.raceId, tab2.numcompletate 
from (SELECT r.constructorId, ra.`year`, r.driverId, r.`position`, r.raceId 
	FROM results r, constructors c, races ra 
	WHERE (r.constructorId = %s AND r.constructorId = c.constructorId 
			AND ra.raceId = r.raceId 
			AND ra.`year` >= %s AND ra.`year` <= %s AND r.`position` IS NOT NULL)) as tab1,
	(SELECT r.constructorId, count(r.`position`) AS numcompletate 
	FROM results r, constructors c, races ra 
	WHERE (r.constructorId =%s AND r.constructorId = c.constructorId 
		AND ra.raceId = r.raceId AND ra.`year` >= %s AND ra.`year` <= %s) 
		and r.`position` is not null
	group by r.constructorId) as tab2
	where tab1.constructorID=tab2.constructorId 
                    """

        cursor.execute(query, (constructorId, anno1, anno2, constructorId, anno1, anno2))
        res = []
        for row in cursor:
            res.append((row["year"], row["driverId"], row["position"], row["raceId"], row["numcompletate"]))

        cursor.close()
        cnx.close()
        return res