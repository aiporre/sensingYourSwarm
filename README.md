# Sensing Your Swarm Project

<p>Picture a thousand mini-robots which sense a dangerous location and this information allows to us determine a secured path although this space and avoid deathly objects in there. This is what our project attempts to display.</p>

<IMG SRC="http://i.dailymail.co.uk/i/pix/2011/08/23/article-0-02D26216000005DC-732_468x375.jpg" ALT="some text" WIDTH=320 HEIGHT=320>------------------<IMG SRC="http://groups.csail.mit.edu/drl/BoeingPages/ResearchProblems/whole-swarm-from-above.jpg" ALT="some text" WIDTH=320 HEIGHT=320>

<h3>Sensign an hazardous location with an swarm of random walkers</h3>

<p>Sensing your swarm proposes an idea that rig out humans to navigate in dangerous environment such as airplanes accidents, shipwrenks and outer space exploring situations. As a bio-inspired robotic system this proyect hands in an prototype which apes the random movement of flies swarms and applies to measurement of risky gases and deathly temperature in hazardous locations, those multiple measurement allows to graph into a web-page based into the combination of Ethernet and SPI protocol network, a secure path throughout field skipping obstacles. Furthermore, in this project a main robot performs as seeing eye dog which could guide a person along the secured path, while it plays the role of gateway towards the server interpreting multiplied nodes composed by each measurement terminal.</p>

<h3>Robotic comunication architecture toward user</h3>

<p>The robotic system's architecture is divided in four layers. At the lower place lies the mini-robots(miniBots) which randomly measure an field. Each of this independent units carries two sensors: one used to measure dangerous gases as butane or monoxide, and the otherone used to measure temperature levels. Moreover, each of these units also incopores and RF-module which based on the SPI protocol builds an strar-shaped network architecture that sends all the information toward the next layer on that protocol. In the next layer, it is the guide-gateway robot (GGBot) who channels all the information toward the server using an http-post into json object, every post contains the identifier and the measurements asociated to each idenfier. Over the GGBot is the "Positioning Supervision System" which determines the position of each robot including the GGBot, it uses a camera and computacional color filters in order to identify each unit based on it's color. Finaly, on the top it is placed the GUI and mapping system that displays the heat map and determines the path throughout the field based on repulsive funtions path planning algorithms.</p>

<a href="http://es.tinypic.com?ref=25jcsco" target="_blank"><img src="http://i57.tinypic.com/25jcsco.jpg" border="0" alt="Image and video hosting by TinyPic"></a>
