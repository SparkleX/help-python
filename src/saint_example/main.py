from sanic import Sanic
from sanic.response import json, text

app = Sanic("MyHello")

@app.on_request
async def run_before_handler(request):
    print("run_before_handler")


@app.route("/")
async def test(request):
    return json("world")

@app.route('/hi')
async def hi_my_name_is(request):
    return text("Hi, my name is {}".format(request.ctx))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)