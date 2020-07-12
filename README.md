# Desk LED Changer

This Python script reads the screen pixels in a 200x200 area, averages the colors and then updates a bulb every <1/2/10> seconds via the Home Assistant API. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python 3.7+
* pip3
* Pytest
* A Home Assistant server that has access to your light bulb/LEDs

### Installing

#### This assumes that you have a Home Assistant server already up and running

Clone this repro
`git clone https://github.com/insidus341/DeskLEDs.git`

Install the PIP3 requirements
`pip3 install -r requirements.txt`

Install Pytest
`pip3 install pytest`

Change the configuration.txt file to match your environment

## Running the tests

`pytest tests/`

## Deployment

Run the script with
`python3 -m run.app` (Mac/Linux)
`py -m run.app` (Windows)

## Built With

* [VsCode](https://code.visualstudio.com/) - The web framework used

## Contributing

Please make a pull request if you'd like to contribute

## Authors

* **James Earl** - *Initial work* - [Insidus341](https://github.com/Insidus341)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
