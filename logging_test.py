import logging
import pandas as pd

logging.basicConfig(filename="logger_sample.txt", level=logging.DEBUG, filemode='w',
                    format='%(asctime)s:%(levelname)s:%(message)s')

logging.debug("This is DEBUG")
logging.info("This is info")
logging.warning("This is warning")
logging.error("This is error")
logging.critical("This is critical")


def read_file(path, file_type):
    global df
    try:
        if file_type == 'csv':
            df = pd.read_csv(path)
            rows = df.shape[0]
            print("CSV file read successfully", path)
            logging.info(f"CSV File read successfully {path} and rows read is {rows}")
        elif file_type == 'xlsx':
            df = pd.read_excel(path)
            print("Excel file read successfully", path)
            logging.info(f"Excel File read successfully +{path}")
        elif file_type == 'json':
            df = pd.read_json(path)
            print("json file read successfully", path)
            logging.info(f"json File read successfully +{path}")
        else:
            pass
        return df
    except:
        error_files = []
        error_files.append(path)
        print(error_files)
        logging.critical("File is not present")


ds = read_file("D:/learning/Python/Contact_info.csv", 'csv')
print(ds)
