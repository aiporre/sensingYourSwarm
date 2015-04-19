# Sensing Your Swarm Project

<p>Picture a thousand mini-robots which sense a dangerous location and this information allows to us determine a secured path although this space and avoid deathly objects in there. This is what our project attempts to display.</p>

<IMG SRC="http://i.dailymail.co.uk/i/pix/2011/08/23/article-0-02D26216000005DC-732_468x375.jpg" ALT="some text" WIDTH=320 HEIGHT=320>---------<IMG SRC="http://groups.csail.mit.edu/drl/BoeingPages/ResearchProblems/whole-swarm-from-above.jpg" ALT="some text" WIDTH=320 HEIGHT=320>

<h3>Sensign an hazardous location with an swarm of random walkers</h3>

<p>Sensing your swarm proposes an idea that rig out humans to navigate in dangerous environment such as airplanes accidents, shipwrenks and outer space exploring situations. As a bio-inspired robotic system this proyect hands in an prototype which apes the random movement of flies swarms and applies to measurement of risky gases and deathly temperature in hazardous locations, those multiple measurement allows to graph into a web-page based into the combination of Ethernet and SPI protocol network, a secure path throughout field skipping obstacles. Furthermore, in this project a main robot performs as seeing eye dog which could guide a person along the secured path, while it plays the role of gateway towards the server interpreting multiplied nodes composed by each measurement terminal.</p>

<h3>Robotic comunication architecture toward user</h3>

<p>The robotic system's architecture is divided in four layers. At the lower place lies the mini-robots(miniBots) which randomly measure an field. Each of this independent units carries two sensors: one used to measure dangerous gases as butane or monoxide, and the otherone used to measure temperature levels. Moreover, each of these units also incopores and RF-module which based on the SPI protocol builds an strar-shaped network architecture that sends all the information toward the next layer on that protocol. In the next layer, it is the guide-gateway robot (GGBot) who channels all the information toward the server using an http-post into json object, every post contains the identifier and the measurements asociated to each idenfier. Over the GGBot is the Positioning Supervision System (PS system) which determines the position of each robot including the GGBot, it uses a camera and computacional color filters in order to identify each unit based on it's color. Finaly, on the top it is placed the GUI and mapping system that displays the heat map and determines the path throughout the field based on repulsive funtions path planning algorithms.</p>

<a href="http://es.tinypic.com?ref=25jcsco" target="_blank"><img src="http://i57.tinypic.com/25jcsco.jpg" border="0" alt="Image and video hosting by TinyPic"></a>
<h4>MiniBots</h4>
<p>Mini-bots are hacked Chinese toys which had been reconstructed with addition of two sensors:  a temperature sensor LM35 in full range configuration and a dangerous gas sensor XXX which can measure butane, CO2 and CO concentrations with a very good precision. Also, each of these robots are equipped with a RF module, such element allows to mini-robot sent its measurement toward the user's screen. Lastly an arduino-nano controls measurement and  communication functions on the mini-bot. </p>
<h4>GGBot</h4>
<p>The GGBoy plays two main funcions into the robotic system. First, it integrates all the information  as the central node into a star shaped communication architecture. Basically all the measurement nodes, which are the mini-bots, are SPI slaves sending information to an SPI Master module constituted by another RF module connected to a RaspBerry Pi B+. Futhermore, the latter also is connected to an Wi-Fi network that allows to send all the measurement into an json object which is being interpreted by the Back-End algorithm on the user interface. Second, not implemented but hoping in the final model, the GGBot performs the human guiding functions. In the matter of fact, based on the on the map it shall to steer human along the secure path.</p>
<p>To navigate an determine objects on his way, the GGBot uses an laser position measurement system. This system is based into an laser pointer and an RapiCam. As the figure shows, the laser is aiming into a secant line to focal axis of the camera, and using trigonometric operations the RaspBerry calculates the distance of an obstacle in front the camera based on the movement of the laser point on projection plane.</p>
<h4>Inside of the PS System</h4>
<p>Alongside, the PS system determines the position of all the robots based on the position of color marks on the robots. That is using colored squares on the top of the robots and a HD-cam this system calculates the position based on morphological and color filters embedded into the Open CV library. All the code have been written in C++ to ensure an soft real time calculation.  Besides, the PS system is also connected to the Wi-Fi network and sends posts on jsons objects which contain the position of each robot that information is used to graph and potential field of heat which represents the temperature mantle over the field.</p>
<h4>presenting the dish: Graphical User Interface</h4>
<h4>Secured path planing</h4>



