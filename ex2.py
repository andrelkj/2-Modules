# Agendamento de desligamento

# Crie duas funções em python para agendar o desligamento do computador em uma hora e meia hora.
import os


# Agenda o desligamento após determinado tempo em minutos
def schedule_shutdown_in_minutes(minutes):
    os.system(f"sudo shutdown -h +{minutes}")


# Agenda desligamento para um horário determinado
def schedule_shutdown_for_hour(hour):
    os.system(f"sudo shutdown -h {hour}")


# Cancela desligamentos agendados
def cancel_scheduled_shutdown():
    os.system("sudo killall shutdown")


# Verificar desligamentos agendados
def retrieve_scheduled_shutdowns():
    output = os.popen("ps aux | grep [s]hutdown").read()
    if output:
        print("Scheduled shutdowns found:")
        print(output)
    else:
        print("No scheduled shutdowns found.")


schedule_shutdown_in_minutes(30)
schedule_shutdown_for_hour("00:00")
cancel_scheduled_shutdown()
retrieve_scheduled_shutdowns()
