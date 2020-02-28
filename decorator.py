def use_logging(level):
	def decorator(func):
		def wrapper(*args, **kwargs):
			if level == "warn":
				print("%s is running %s" % (func.__name__, "warn"))
			elif level == "info":
				logging.info("%s is running %s" % (func.__name__, "info"))
			return func(*args)
		return wrapper

	return decorator

@use_logging(level="warn")
def foo(name='foo'):
	print("i am %s" % name)
	
if __name__ == "__main__":
	foo('beibei')