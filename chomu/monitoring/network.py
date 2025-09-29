import psutil

def get_service_connections(pid):
    try:
        proc = psutil.Process(pid)
        conns = proc.connections(kind='inet')
        return [
            {
                'fd': c.fd,
                'family': str(c.family),
                'type': str(c.type),
                'laddr': c.laddr,
                'raddr': c.raddr if c.raddr else None,
                'status': c.status
            }
            for c in conns
        ]
    except Exception as e:
        return []
