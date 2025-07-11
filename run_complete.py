import subprocess
import sys
import time
from threading import Thread

def run_api():
    """Ejecutar API en thread separado"""
    subprocess.run([sys.executable, "-m", "app.main"])

def run_worker():
    """Ejecutar Worker en thread separado"""
    time.sleep(2)  # Esperar que API inicie
    subprocess.run([sys.executable, "-m", "app.worker"])

if __name__ == "__main__":
    print("🚀 Iniciando Logs Microservice completo...")
    
    # Iniciar API en thread
    api_thread = Thread(target=run_api, daemon=True)
    api_thread.start()
    
    # Iniciar Worker en thread
    worker_thread = Thread(target=run_worker, daemon=True)
    worker_thread.start()
    
    try:
        # Mantener proceso principal vivo
        api_thread.join()
        worker_thread.join()
    except KeyboardInterrupt:
        print("\n🛑 Deteniendo servicios...")
        sys.exit(0)