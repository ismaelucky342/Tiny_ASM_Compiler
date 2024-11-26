# Variables
PYTHON := python3
SRC_DIR := src
ENTRY_POINT := $(SRC_DIR)/main.py

# Reglas principales
.PHONY: menu run test clean install

# Menú interactivo
menu:
	@echo "===========================";
	@echo "        Opciones           ";
	@echo "===========================";
	@echo "1. Compilar el proyecto"
	@echo "2. Ejecutar el programa principal";
	@echo "3. Limpiar archivos temporales";
	@echo "4. Instalar dependencias";
	@echo "5. Salir";
	@echo "===========================";
	@read -p 'Seleccione una opción (1-4): ' opt; \
	case $$opt in \
		1) make compile ;; \
		2) $(MAKE) run ;; \
		3) $(MAKE) clean ;; \
		4) $(MAKE) install ;; \
		5) echo "Saliendo..."; exit 0 ;; \
		*) echo "Opción inválida. Intente nuevamente." ;; \
	esac

compile:
	@echo "Compilando el proyecto..."
	@python3 -m py_compile src/*.py
	@echo "Compilación completada."

run:
	@echo "Ejecutando el proyecto..."
	@python3 src/main.py
	@echo "Ejecución finalizada."


clean:
	@echo "Limpiando archivos generados..."
	@find . -name "__pycache__" -type d -exec rm -rf {} +
	@echo "Limpieza completada."


# Instalar dependencias
install:
	@pip install -r requirements.txt
	@echo "Dependencias instaladas."
