from flask import Flask, render_template, request, redirect, url_for, make_response
import json
import urllib
import networkx as nx

app = Flask(__name__)

@app.route('/twitter-brexit-1')
def twitterBrexit1():
    return render_template('twitter_brexit_1.html')

@app.route('/twitter-brexit-2')
def twitterBrexit2():
    return render_template('twitter_brexit_2.html')

@app.route('/twitter-brexit-3')
def twitterBrexit3():
    return render_template('twitter_brexit_3.html')

@app.route('/twitter-brexit-4')
def three():
    gravity = 0.4
    repetitions = 0
    return render_template('twitter_brexit_3.html', gravity = gravity, repetitions = repetitions)

@app.route('/data')
def graph_to_json():

    json_file = {}

    position_file = 'https://s3-us-west-2.amazonaws.com/pollstr/visuals/dataBrexit.txt'
    open_s3 = urllib.URLopener()
    position = eval(open_s3.open(position_file).read())

    neighborhood_file = 'https://s3-us-west-2.amazonaws.com/pollstr/visuals/net4.txt'
    open_s3 = urllib.URLopener()
    neighborhood_dict = eval(open_s3.open(neighborhood_file).read())

    Graph = nx.from_dict_of_lists(neighborhood_dict)

    nodes = Graph.nodes()
    list_of_nodes = []

    id_of_nodes = {}
    i = 0
    for node in nodes:
        id_of_nodes[node] = i
        i += 1

    node_info_dict = {}

    for node in nodes:
        node_info = {}
        node_info['name'] = str(node)
        try:
            if position[node]['position'] == 'leave':
                node_info['color'] = 'blue'
                node_info['followers'] = position[node]['followers']
                node_info['logFollowers'] = position[node]['log']

            elif position[node]['position'] == 'remain':
                node_info['color'] = 'yellow'
                node_info['followers'] = position[node]['followers']
                node_info['logFollowers'] = position[node]['log']
            else:
                node_info['color'] = '#e7e7e7'
                node_info['followers'] = position[node]['followers']
                node_info['logFollowers'] = position[node]['log']
        except:
            node_info['color'] = '#e7e7e7'
            node_info['followers'] = 'DK'
            node_info['logFollowers'] = 3
        node_info_dict[str(node)] = node_info

        list_of_nodes.append(node_info)

    edges = Graph.edges()
    list_of_edges = []
    for node in nodes:
        neighbors = Graph.neighbors(node)
        for neighbor in neighbors:

            edge_info = {}
            edge_info['source'] = id_of_nodes[node]
            edge_info['target'] = id_of_nodes[neighbor]
            edge_info['value'] = 1
            try:
                edge_info['color'] = node_info_dict[node]['color']
            except:
                edge_info['color'] = '#e7e7e7'
            list_of_edges.append(edge_info)

    json_file['nodes'] = list_of_nodes
    json_file['links'] = list_of_edges

    json_file = json.dumps(json_file)

    return json_file

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port="8000")
