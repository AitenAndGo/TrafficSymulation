import simulation
from window import Window


# flara = engine.GameObject(50, 50)
# flara.set_image("images/flara.png")
# flara.rotate(70)
# flara.acceleration = engine.Vector(-10, 0)
# flara.velocity = engine.Vector(100, 0)
#
# rec = engine.GameObject(100, 100)
# rec.rectangular_shape(20, 20)
# rec.color(255, 0, 100)

sim = simulation.Simulation()
sim.generateCars(250)
window = Window(sim)
window.run()
