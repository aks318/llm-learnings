def gen():
    yield "first"
    yield "second"
    yield "third"


print(gen())
gen()
gen()