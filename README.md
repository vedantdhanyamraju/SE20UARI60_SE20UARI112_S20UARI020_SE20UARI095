# SE20UARI60_SE20UARI112_S20UARI020_SE20UARI095

We are interfacing with an Infrared (IR) sensor connected to a Raspberry Pi's GPIO pin. 
An IR (Infrared) sensor, also known as an IR receiver or IR detector, is an electronic component that is used to detect infrared radiation in its vicinity. Infrared radiation is a form of electromagnetic radiation that has a wavelength longer than visible light but shorter than radio waves. IR sensors are commonly used in various applications due to their ability to detect the presence or absence of IR signals, which can be emitted by objects, remote controls, or other sources

Here's a brief overview of what we have done in the code:

1)Sensor Setup: We specify that the IR sensor is connected to GPIO pin 16 on the Raspberry Pi.

2)GPIO Configuration: We configure the GPIO pin as an input pin, which means it will be used to read signals from the IR sensor.

3)Continuous Reading: Our code enters an infinite loop, where it continually checks the state of the IR sensor.

4)State Detection: Within the loop, we use GPIO.input(IR_sensor) to read the state of the IR sensor. It will return either 0 (LOW) or 1 (HIGH) based on whether the sensor detects an infrared signal or not.

5)Print State: The script then prints the state of the IR sensor to the console, allowing us to see whether the sensor is currently detecting an infrared signal or not.

6)Delay: After each sensor reading, there is a 0.1-second delay (time.sleep(0.1)) to ensure that the script doesn't read the sensor too rapidly.

7)Keyboard Interrupt Handling: We've included an exception handler to catch a KeyboardInterrupt (triggered by pressing Ctrl+C). When this occurs, the script will clean up GPIO resources, ensuring that they are properly released.

8)In essence, our code continuously monitors the IR sensor's state and reports it in real-time. This can be useful for various applications such as detecting the presence of objects, receiving input from an IR remote control, or any other situation where we need to know whether the sensor is active or not.
