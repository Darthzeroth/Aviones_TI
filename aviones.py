import pymongo
from pymongo import MongoClient
from pprint import pprint

# Asignación del púerto que usa MongoDB
client = MongoClient("localhost", 27017)
# creacion de la bd
db = client["agencias"]


# imprime los nombres de las colecciones creadas
print(db.list_collection_names())


def run():

    # añadiendo colecciones
    agencias = db.agencias

    agencia1 = {
        "_id": 1,
        "nombre_agencia": "Vuelos internacionales",
        "direccion": "Calle Valladolid 76, Puebla",
        "fax": "Vuentern@123",
        "web": "Vuelosinternacionales.com",
        "hoteles": [
            {
                "nombreHotel": "El descanso",
                "direccionHotel": "7 oriente 206",
                "categoria": "5 Estrellas",
                "ofertas": [
                    {
                        "nombreOferta": "Pareja",
                        "descripcion": "Habitacion sencilla con baño, cama matrimonial",
                        "precio": 500
                    },
                    {
                        "nombreHotel": "Comelon",
                        "direccionHotel": "Habitacion sencilla con baño, cama matrimonial, buffet de desayuno",
                        "categoria": 700
                    },
                ],
                "excursionProlongada": [
                    {
                        "lugar": "Fuertes de Loreto",
                        "diaSemana": "Viernes-Sabado",
                        "horaSalida": "12 pm",
                        "tipo": "Larga"
                    },
                ]
            },
            {
                "nombreHotel": "El retiro",
                "direccionHotel": "9 oriente 207",
                "categoria": "4 Estrellas",
                "ofertas": [
                    {
                        "nombreOferta": "Semana Santa",
                        "descripcion": "40% DESCUENTO",
                        "precio": 300
                    },
                    {
                        "nombreHotel": "Reserva anticipada",
                        "direccionHotel": "Habitacion sencilla con baño, cama matrimonial, buffet de desayuno",
                        "categoria": 300
                    },
                ]
            },
        ],
        "excursiones": [
            {
                "lugar": "Fuertes de Loreto",
                "diaSemana": "Viernes",
                "horaSalida": "12 pm",
                "tipo": "Corta"
            },
            {
                "lugar": "Cuexcomate",
                "diaSemana": "Sabados",
                "horaSalida": "11 am",
                "tipo": "Corta"
            }
        ],
        "turistas": [
            {
                "_idTurista": 1,
                "nombre": "Oscar Gonzalez",
                "nacionalidad": "Mexicana",
                "tipo": "Individual",
                "reserva": [
                    {
                        "compañiaAerea": "Aero Mexico",
                        "hoteles": [
                            {
                                "nombreHotel": "El descanso",
                                "fechas": [
                                    {
                                         "fechaLlegada": "10/01/2020",
                                         "fechaSalida": "12/01/2020"
                                    }
                                ]
                            },
                            {
                                "nombreHotel": "El rincon",
                                "fechas": [
                                    {
                                        "fechaLlegada": "14/01/2020",
                                        "fechaSalida": "16/01/2020"
                                    }
                                ]
                            },

                        ],
                        "CantidadAcompanantes": 5,
                        "precioTotal": 50000
                    }
                ]
            },
            {
                "_idTurista": 2,
                "nombre": "Luis Perez",
                "nacionalidad": "Mexicana",
                "tipo": "Grupo",
            },
            {
                "_idTurista": 3,
                "nombre": "Martina Suarez",
                "nacionalidad": "Italiana",
                "tipo": "Cientifico",
            },
        ],
        "paquetes": [
            {
                "codigo": 1,
                "duracion": "3 dias",
                "facilidades": "3",
                "descipcion": "Tres dias de reserva",
                "precio": 500,
                "reservacion": [
                    {
                        "companiaAerea": "Aero Mexico",
                        "fechaSalida": "02/01/2020",
                        "CantParticipantes": 5,
                        "precioTotal": 25000
                    }
                ]
            },
            {
                "codigo": 2,
                "duracion": "2 dias",
                "facilidades": "2",
                "descipcion": "Reserva 2 dias y 1 excursion",
                "precio": 700,
                "reservacion": [{
                    "companiaAerea": "Aero Star",
                    "fechaSalida": "02/05/2020",
                    "CantParticipantes": 8,
                    "precioTotal": 48000
                }

                ]
            },
            {
                "codigo": 3,
                "duracion": "1 semana",
                "facilidades": "Hospedaje, incluyendo desayuno buffet y una excursion",
                "descipcion": "Cientifico",
                "precio": 600,
                "reservacion": [{
                    "companiaAerea": "Aero Bonita",
                    "fechaSalida": "02/10/2020",
                    "CantParticipantes": 10,
                    "precioTotal": 6000
                }

                ]
            }
        ],



    }

    # inserta varios documentos a la vez en la coleccion
    #registros_agencias = agencias.insert_many([agencia1])
    for registro in agencias.find({"hoteles.nombreHotel":"El descanso"}):
        pprint(registro)
    


if __name__ == '__main__':
    run()
