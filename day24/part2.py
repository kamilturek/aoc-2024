import re
import sys

import graphviz


def get_value(wire, wires):
    x = wires[wire]
    if isinstance(x, tuple):
        in1, op, in2 = x
        in1 = get_value(in1, wires)
        in2 = get_value(in2, wires)
        return op(in1, in2)
    return x


def draw(out, wires, graph, edges):
    graph.node(out)

    if out not in wires:
        return

    in1, op, in2 = wires[out]
    gate_id = f"{in1}{op}{in2}"
    graph.node(gate_id, op)

    if (out, gate_id) not in edges:
        graph.edge(out, gate_id)
        edges.add((out, gate_id))

    graph.node(in1)
    graph.node(in2)

    if (gate_id, in1) not in edges:
        graph.edge(gate_id, in1)
        edges.add((gate_id, in1))

    if (gate_id, in2) not in edges:
        graph.edge(gate_id, in2)
        edges.add((gate_id, in2))

    draw(in1, wires, graph, edges)
    draw(in2, wires, graph, edges)


def solve(input):
    """
    gst,khg,nhn,tvb,vdc,z12,z21,z33
    """
    wires = {}
    zlen = 0

    gates = input.read().split("\n\n")[1].splitlines()
    for gate in gates:
        in1, op, in2, out = re.match(
            r"([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)", gate
        ).groups()
        wires[out] = (in1, op, in2)

        if out.startswith("z"):
            zlen = max(zlen, int(out[1:]) + 1)

    edges = set()
    graph = graphviz.Digraph(format="png")

    for z in range(zlen):
        draw(f"z{z:0>2}", wires, graph, edges)

    graph.render("output/circuit.gv")


if __name__ == "__main__":
    print(solve(sys.stdin))
