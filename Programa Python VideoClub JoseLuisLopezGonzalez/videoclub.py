"""Este programa lee un archivo Csv con datos de películas y convierte cada registro en formato Xml compatible con Odoo."""
def generate_unique_id(counter):
    """ ID único para cada registro."""
    return f"film_{counter}"

def format_actors(actors_string):
    """Esto permite convertir una cadena de actores en el formato Xml de Odoo."""
    actors_list = actors_string.split('-')
    formatted_actors = ', '.join([f"ref('{actor.strip()}')" for actor in actors_list])
    return f"[(6,0,[{formatted_actors}])]"

def generate_xml_record(record_id, name, director, actors, release_date, country, duration, rating, file_path):
    """Aqui genera el Xml para un registro de cada película."""
    return f"""    <record id="{record_id}" model="videoclub.peliculas">
        <field name="name">{name}</field>
        <field name="director" ref="{director}" />
        <field name="actors" eval="{actors}" />
        <field name="release">{release_date}</field>
        <field name="country">{country}</field>
        <field name="duration">{duration}</field>
        <field name="rating">{rating}</field>
        <field file="{file_path}" name="cover" type="base64" />
    </record>"""

def main(csv_path, xml_output_path):
    """Lee el archivo CSV  necesario y nos genera el archivo Xml en el formato requerido para Odoo."""
    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            xml_content = "<odoo>\n  <data>\n"
            counter = 1

            for line in csv_file:
                try:
                    fields = line.strip().split(',')
                    if len(fields) != 8:
                        raise ValueError("Número de campos incorrecto en el CSV.")
                    
                    # Asigna las variables necesarias a los campos de Csv.
                    name, director, actors, release_date, country, duration, rating, file_path = fields
                    record_id = generate_unique_id(counter)
                    actors_formatted = format_actors(actors)

                    # Utiliza el Xml para cada registro.
                    xml_content += generate_xml_record(
                        record_id, name, director, actors_formatted, release_date, country, duration, rating, file_path
                    ) + "\n"
                    counter += 1
                except Exception as e:
                    print(f"Error procesando la línea: {line}\nDetalles: {e}")
                    continue

            xml_content += "  </data>\n</odoo>"
            
            # Archivo Xml creado.
            with open(xml_output_path, 'w', encoding='utf-8') as xml_file:
                xml_file.write(xml_content)

            print("Transformación realizada con éxito.")

    except FileNotFoundError:
        print(f"No se encontró el archivo {csv_path}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejecucion del programa y salida de bdpeliculas.xml.
if __name__ == "__main__":
    main("bdpeliculas.csv", "bdpeliculas.xml")
