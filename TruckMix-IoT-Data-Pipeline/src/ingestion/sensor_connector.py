import serial

def connect_to_sensor(port, baud_rate):
    """
    Establishes connection to the SMT32 microcontroller to read pressure sensor data.

    Args:
        port (str): The serial port to which the SMT32 is connected.
        baud_rate (int): The baud rate for the serial communication.

    Returns:
        serial.Serial: The serial connection object.
    """
    try:
        connection = serial.Serial(port, baud_rate, timeout=1)
        print(f"Connected to SMT32 on port {port} with baud rate {baud_rate}")
        return connection
    except serial.SerialException as e:
        print(f"Failed to connect to SMT32: {e}")
        return None

def read_pressure_data(connection):
    """
    Reads pressure sensor data from the SMT32 microcontroller.

    Args:
        connection (serial.Serial): The serial connection object.

    Returns:
        str: The pressure sensor data read from the SMT32.
    """
    if connection and connection.is_open:
        try:
            data = connection.readline().decode('utf-8').strip()
            return data
        except Exception as e:
            print(f"Failed to read data: {e}")
            return None
    else:
        print("Connection is not open.")
        return None

# Example usage
if __name__ == "__main__":
    port = 'COM3'  # Replace with your actual port
    baud_rate = 9600  # Replace with your actual baud rate
    connection = connect_to_sensor(port, baud_rate)
    
    if connection:
        while True:
            pressure_data = read_pressure_data(connection)
            if pressure_data:
                print(f"Pressure Data: {pressure_data}")