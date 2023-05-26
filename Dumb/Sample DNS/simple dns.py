'''
☻ » Probably Not So Simple Now That I Think About It DNS Server « ☻
☻ »                          02/05/2023                         « ☻
'''

import time
import sqlite3 # This is currently mixed with local db stuff

class whois:
    def __init__(self):
        self.whoisData = {} # Soon depreciated
        self.con = sqlite3.connect("dns.db")
        self.cur = self.con.cursor()

    def fetch(self, domain, useSSL=False): # DNS Lookup
        start = time.time()

        try:
            resEnd = self.cur.execute(f"SELECT endpoint FROM dns_url WHERE EXISTS(SELECT domain FROM dns_url WHERE domain = '{domain}')")
            resp = resEnd.fetchone()

            return resp # no workies
        except Exception as e:
            return e

        if domain in self.whoisData:
            out = []
            out.append(domain)
            out.append(self.whoisData[domain])
            out.append(f"{int(round(time.time()-start, 0))}ms")
            return out
        else:
            return None

    def update(self, domain, endpoint, owner="Example"): # Update A Domain - Should probably add auth if was real thing
        start =  time.time()
        if domain in self.whoisData:
            self.whoisData[domain] = endpoint

            out = []
            out.append(domain)
            out.append(self.whoisData[domain])
            out.append(f"{int(round(time.time()-start, 0))}ms")
            return out
        else:
            return None

    def new(self, domain, endpoint, owner="Example"): # Add to the DNS List
        start =  time.time()

        try:
            res = self.cur.execute(f"SELECT * FROM dns_url WHERE domain = {domain}")
            res.fetchone()
        except:
            self.cur.execute("INSERT INTO dns_url(domain, endpoint, owner) VALUES (?,?,?)", (domain, endpoint, owner,))
            self.con.commit()

        if domain not in self.whoisData:
            self.whoisData[domain] = endpoint
            out = []
            out.append(domain)
            out.append(self.whoisData[domain])
            out.append(f"{int(round(time.time()-start, 0))}ms")
            return out
        else:
            return None

class run:
    def fetch(domain, useSSL=False):
        return f"Fetch  | {dns.fetch(domain)}"
    def update(domain, endpoint):
        return f"Update | {dns.update(domain, endpoint, owner)}"
    def new(domain, endpoint, owner="Example"):
        return f"New    | {dns.new(domain, endpoint, owner)}"


dns = whois() # Initialise whois because good coding therefore can theoretically have multiple dns servers running in one?
while True:
    opt = input("Do?\n-> ").lower()[:1]
    if opt == "f":
        print(run.fetch(input("Domain\n-> ")))
    elif opt == "u":
        print(run.update(input("Domain\n-> "), input("Endpoint\n-> "), input("Owner (Example)\n-> ")))
    elif opt == "n":
        print(run.new(input("Domain\n-> "), input("Endpoint\n-> "), input("Owner (Example)\n-> ")))
    else:
        print("\n\nInvalid Option\n\n")