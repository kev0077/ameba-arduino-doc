Class DHT
=========

.. contents::
  :local:
  :depth: 2

**DHT Class**
-------------

**Description**
~~~~~~~~~~~~~~~

A class to use DHT temperature and humidity sensors.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class DHT

**Members**
~~~~~~~~~~~

+-----------------------------+-----------------------------------------+
| **Public Constructors**                                               |
+=============================+=========================================+
| DHT::DHT                    | Constructs a DHT object                 |
+-----------------------------+-----------------------------------------+
| **Public Methods**                                                    |
+-----------------------------+-----------------------------------------+
| DHT::begin                  | Initialize the DHT sensor by setting up |
|                             | the sensor GPIO pin and                 |
|                             | set pull timings.                       |
+-----------------------------+-----------------------------------------+
| DHT::readTemperature        | Read temperature (Fahrenheit or         |
|                             | Celsius) from the DHT sensor            |
+-----------------------------+-----------------------------------------+
| DHT::convertCtoF            | Convert a value from Celsius to         |
|                             | Fahrenheit                              |
+-----------------------------+-----------------------------------------+
| DHT::convertFtoC            | Convert a value from Fahrenheit to      |
|                             | Celsius                                 |
+-----------------------------+-----------------------------------------+
| DHT::readHumidity           | Read humidity value from the DHT sensor |
|                             | as percentage.                          |
+-----------------------------+-----------------------------------------+
| DHT::computeHeatIndex       | Compute the HeatIndex from the readings |
|                             | (Using both Rothfusz and Steadman's     |
|                             | equations)                              |
+-----------------------------+-----------------------------------------+
| DHT::read                   | Check if the sensor is readable         |
+-----------------------------+-----------------------------------------+

**DHT::DHT**
------------

**Description**
~~~~~~~~~~~~~~~

Constructs a DHT object.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    DHT(uint8_t pin, uint8_t type, uint8_t count);

**Parameters**
~~~~~~~~~~~~~~

``pin``: selected GPIO pin on Ameba board. (Default: 8)

``type``: The DHT sensor type. Available sensor types: DHT11, DHT22 (AM2302, AM2321), or DHT21(AM2301). (Default: DHT11)

``count``: The count is ignored as the DHT reading algorithm adjusts itself based on the speed of the processor. Default value is 6 (Refer to function declaration in DHT.h)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DHTTester <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/GPIO/examples/DHT_Tester/DHT_Tester.ino>`_

.. note :: "DHT.h" must be included to use the class function.

**DHT::begin**
--------------

**Description**
~~~~~~~~~~~~~~~

Initialize the DHT sensor by setting up the sensor GPIO pin and set pull timings.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin(uint8_t usec);

**Parameters**
~~~~~~~~~~~~~~

``usec``: Optionally pass pull-up time (in microseconds) before DHT reading starts. (Default: 55, see function declaration in DHT.h)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DHTTester <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/GPIO/examples/DHT_Tester/DHT_Tester.ino>`_

.. note :: "DHT.h" must be included to use the class function.

**DHT::readTemperature**
------------------------

**Description**
~~~~~~~~~~~~~~~

Read temperature (Fahrenheit or Celsius) from the DHT sensor in selected scale.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    float readTemperature(bool S, bool force);

**Parameters**
~~~~~~~~~~~~~~

``S``: Scale for temperature, available values: True (Fahrenheit) and False (Celsius). (Default: False, see function declaration in DHT.h)

``force``: Enable or disable force mode, available values: True (Force mode) and False (Disable force mode). (Default: False, see function declaration in DHT.h)

**Returns**
~~~~~~~~~~~

This function returns the current temperature as a float value in selected scale.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DHTTester <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/GPIO/examples/DHT_Tester/DHT_Tester.ino>`_

.. note :: "DHT.h" must be included to use the class function.

**DHT::convertCtoF**
--------------------

**Description**
~~~~~~~~~~~~~~~

Convert a temperature value from Celsius to Fahrenheit.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    float convertCtoF(float c);

**Parameters**
~~~~~~~~~~~~~~

``c``: Temperature in Celsius.

**Returns**
~~~~~~~~~~~

This function returns the temperature in Fahrenheit as a float number.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DHTTester <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/GPIO/examples/DHT_Tester/DHT_Tester.ino>`_

.. note :: "DHT.h" must be included to use the class function.

**DHT::convertFtoC**
--------------------

**Description**
~~~~~~~~~~~~~~~

Convert a temperature value from Fahrenheit to Celsius.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    float convertFtoC(float f);

**Parameters**
~~~~~~~~~~~~~~

``f``: Temperature in Fahrenheit.

**Returns**
~~~~~~~~~~~

This function returns the temperature in Celsius as a float number.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DHTTester <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/GPIO/examples/DHT_Tester/DHT_Tester.ino>`_

.. note :: "DHT.h" must be included to use the class function.

**DHT::readHumidity**
---------------------

**Description**
~~~~~~~~~~~~~~~

Read humidity value from the DHT sensor as percentage.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    float readHumidity(bool force);

**Parameters**
~~~~~~~~~~~~~~

``force``: force read mode. (Default: False, see function declaration in DHT.h)

**Returns**
~~~~~~~~~~~

This function returns current humidity value represented in float as percentage.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DHTTester <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/GPIO/examples/DHT_Tester/DHT_Tester.ino>`_

.. note :: "DHT.h" must be included to use the class function. Reading temperature or humidity takes about 250 milliseconds. Sensor readings may also be up to 2 seconds.

**DHT::computeHeatIndex**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Compute the HeatIndex from the readings (Using both Rothfusz and Steadman's equations). More details refer to `The Heat Index Equation <http://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml>`_

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    float computeHeatIndex(bool isFahrenheit);
    float computeHeatIndex(float temperature, float percentHumidity, bool isFahrenheit = true);

**Parameters**
~~~~~~~~~~~~~~

``temperature``: The temperature value in selected scale.

``percentHumidity``: humidity value in percentage.

``isFahrenheit``: choose temperature vale in Fahrenheit or Celsius. Available values: True (in Fahrenheit) or False (Celsius). (Default: True)

**Returns**
~~~~~~~~~~~

This function returns the heat index in Fahrenheit or Celsius as a float value.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DHTTester <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/GPIO/examples/DHT_Tester/DHT_Tester.ino>`_

.. note :: "DHT.h" must be included to use the class function.

**DHT::read**
-------------

**Description**
~~~~~~~~~~~~~~~

Check if the sensor is readable.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    bool read (bool force);

**Parameters**
~~~~~~~~~~~~~~

``force``:  Enable or disable force mode. Available values: True (Force mode) and False (Disable force mode). (Default: False, see function declaration in DHT.h)

**Returns**
~~~~~~~~~~~

This function returns whether the sensor is readable in every two seconds.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DHTTester <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/GPIO/examples/DHT_Tester/DHT_Tester.ino>`_

.. note :: "DHT.h" must be included to use the class function.
