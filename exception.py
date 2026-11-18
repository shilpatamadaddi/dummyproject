try:
  a = "w"/"q"
  print(a)
except ZeroDivisionError:
  print("cannot dividebyzero")
except TypeError:
    print("unsupported operand type for str")
finally:
    print("run")