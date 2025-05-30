import pandas as pd
import mysql.connector
from database.connection import get_connection
from datetime import datetime

def import_prouni_data():
    # File path and connection
    file_path = 'data/prouniData.csv'
    conn = get_connection()
    cursor = conn.cursor()
    
    print("Reading ProUni dataset...")
    
    try:
        # Read CSV with proper encoding and separator
        df = pd.read_csv(file_path, encoding='latin1', sep=';')
        
        # Filter rows where CODIGO_EMEC_IES_BOLSA equals 1775
        filtered_df = df[df['CODIGO_EMEC_IES_BOLSA'] == 1775]
        
        print(f"Found {len(filtered_df)} entries with IES code 1775")
        
        # Column mapping from CSV to database
        records_inserted = 0
        errors = 0
        
        # Prepare SQL query
        query = """
            INSERT INTO scholarship (
                concession_year, ies_code, ies_name, city, campus,
                scholarship_type, education_mode, course, shift,
                beneficiary_cpf, gender, race, birth_date, has_disability,
                region, state, beneficiary_city
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        # Process each row in the filtered dataframe
        for index, row in filtered_df.iterrows():
            try:
                # Convert birth date from DD/MM/YYYY to YYYY-MM-DD
                birth_date_str = row['DATA_NASCIMENTO']
                birth_date = datetime.strptime(birth_date_str, '%d/%m/%Y').strftime('%Y-%m-%d')
                
                # Convert has_disability from 'S'/'N' to True/False
                has_disability = True if row['BENEFICIARIO_DEFICIENTE_FISICO'] == 'S' else False
                
                # Prepare values for insertion
                values = (
                    int(row['ANO_CONCESSAO_BOLSA']),
                    str(row['CODIGO_EMEC_IES_BOLSA']),
                    row['NOME_IES_BOLSA'],
                    row['MUNICIPIO'],
                    row['CAMPUS'],
                    row['TIPO_BOLSA'],
                    row['MODALIDADE_ENSINO_BOLSA'],
                    row['NOME_CURSO_BOLSA'],
                    row['NOME_TURNO_CURSO_BOLSA'],
                    row['CPF_BENEFICIARIO'],
                    row['SEXO_BENEFICIARIO'],
                    row['RACA_BENEFICIARIO'],
                    birth_date,
                    has_disability,
                    row['REGIAO_BENEFICIARIO'],
                    row['UF_BENEFICIARIO'],
                    row['MUNICIPIO_BENEFICIARIO']
                )
                
                # Execute insert query
                cursor.execute(query, values)
                records_inserted += 1
                
                # Print progress every 10 records
                if records_inserted % 10 == 0:
                    print(f"Inserted {records_inserted} records so far...")
                    
            except Exception as e:
                errors += 1
                print(f"Error processing row {index}: {str(e)}")
        
        # Commit the transaction
        conn.commit()
        print(f"\nImport completed:")
        print(f"- {records_inserted} records successfully inserted")
        print(f"- {errors} records failed to insert")
        
    except Exception as e:
        print(f"Error reading or processing the dataset: {str(e)}")
    finally:
        cursor.close()
        conn.close()