extends RigidBody2D
var f = 500

func _ready():
	
	apply_central_impulse(Vector2(rand_range(-f, f),rand_range(-f,f)))
