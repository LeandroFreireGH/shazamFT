import data_methods as dm
import buscador as bs


if __name__ == '__main__':

    # Descomentar estas lineas para cargar canciones a la base de datos
    # Solo cargar cancions ligeras porque el proceso es muy tardado
    # dm.drop_db()
    # dm.load_db('./data')

    # Direccion del archivo de muestra de audio para realizar la busqueda
    input_wav = 'logic/recording.wav'
    bs.print_matches(input_wav, num_matches=1)
