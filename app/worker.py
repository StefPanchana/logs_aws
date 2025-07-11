import time
from dotenv import load_dotenv
from .container import Container

load_dotenv()

def main():
    container = Container()
    process_log_use_case = container.process_log_use_case
    
    print("Worker iniciado - procesando logs...")
    
    while True:
        try:
            if process_log_use_case.execute():
                print("Log procesado exitosamente")
            else:
                time.sleep(1)
        except Exception as e:
            print(f"Error procesando log: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()