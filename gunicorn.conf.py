import multiprocessing

# Определяем количество воркеров. Рекомендуется использовать (2 * CPU) + 1
workers = multiprocessing.cpu_count() * 2 + 1

# Привязка к адресу и порту
bind = "0.0.0.0:8080"

# Таймаут (в секундах)
timeout = 30

# Логирование
accesslog = "-"  # Выводить access логи в stdout
errorlog = "-"   # Выводить error логи в stderr
loglevel = "info"