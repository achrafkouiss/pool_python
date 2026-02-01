data_dictionary = {
   "players":{
      "alice":{
         "level":41,
         "total_score":2824,
         "sessions_played":13,
         "favorite_mode":"ranked",
         "achievements_count":5
      },
      "bob":{
         "level":16,
         "total_score":4657,
         "sessions_played":27,
         "favorite_mode":"ranked",
         "achievements_count":2
      },
      "charlie":{
         "level":44,
         "total_score":9935,
         "sessions_played":21,
         "favorite_mode":"ranked",
         "achievements_count":7
      },
      "diana":{
         "level":3,
         "total_score":1488,
         "sessions_played":21,
         "favorite_mode":"casual",
         "achievements_count":4
      },
      "eve":{
         "level":33,
         "total_score":1434,
         "sessions_played":81,
         "favorite_mode":"casual",
         "achievements_count":7
      },
      "frank":{
         "level":15,
         "total_score":8359,
         "sessions_played":85,
         "favorite_mode":"competitive",
         "achievements_count":1
      }
   },
   "sessions":[
      {
         "player":"bob",
         "duration_minutes":94,
         "score":1831,
         "mode":"competitive",
         "completed":False
      },
      {
         "player":"bob",
         "duration_minutes":32,
         "score":1478,
         "mode":"casual",
         "completed":True
      },
      {
         "player":"diana",
         "duration_minutes":17,
         "score":1570,
         "mode":"competitive",
         "completed":False
      },
      {
         "player":"alice",
         "duration_minutes":98,
         "score":1981,
         "mode":"ranked",
         "completed":True
      },
      {
         "player":"diana",
         "duration_minutes":15,
         "score":2361,
         "mode":"competitive",
         "completed":False
      },
      {
         "player":"eve",
         "duration_minutes":29,
         "score":2985,
         "mode":"casual",
         "completed":True
      },
      {
         "player":"frank",
         "duration_minutes":34,
         "score":1285,
         "mode":"casual",
         "completed":True
      },
      {
         "player":"alice",
         "duration_minutes":53,
         "score":1238,
         "mode":"competitive",
         "completed":False
      },
      {
         "player":"bob",
         "duration_minutes":52,
         "score":1555,
         "mode":"casual",
         "completed":False
      },
      {
         "player":"frank",
         "duration_minutes":92,
         "score":2754,
         "mode":"casual",
         "completed":True
      },
      {
         "player":"eve",
         "duration_minutes":98,
         "score":1102,
         "mode":"casual",
         "completed":False
      },
      {
         "player":"diana",
         "duration_minutes":39,
         "score":2721,
         "mode":"ranked",
         "completed":True
      },
      {
         "player":"frank",
         "duration_minutes":46,
         "score":329,
         "mode":"casual",
         "completed":True
      },
      {
         "player":"charlie",
         "duration_minutes":56,
         "score":1196,
         "mode":"casual",
         "completed":True
      },
      {
         "player":"eve",
         "duration_minutes":117,
         "score":1388,
         "mode":"casual",
         "completed":False
      },
      {
         "player":"diana",
         "duration_minutes":118,
         "score":2733,
         "mode":"competitive",
         "completed":True
      },
      {
         "player":"charlie",
         "duration_minutes":22,
         "score":1110,
         "mode":"ranked",
         "completed":False
      },
      {
         "player":"frank",
         "duration_minutes":79,
         "score":1854,
         "mode":"ranked",
         "completed":False
      },
      {
         "player":"charlie",
         "duration_minutes":33,
         "score":666,
         "mode":"ranked",
         "completed":False
      },
      {
         "player":"alice",
         "duration_minutes":101,
         "score":292,
         "mode":"casual",
         "completed":True
      },
      {
         "player":"frank",
         "duration_minutes":25,
         "score":2887,
         "mode":"competitive",
         "completed":True
      },
      {
         "player":"diana",
         "duration_minutes":53,
         "score":2540,
         "mode":"competitive",
         "completed":False
      },
      {
         "player":"eve",
         "duration_minutes":115,
         "score":147,
         "mode":"ranked",
         "completed":True
      },
      {
         "player":"frank",
         "duration_minutes":118,
         "score":2299,
         "mode":"competitive",
         "completed":False
      },
      {
         "player":"alice",
         "duration_minutes":42,
         "score":1880,
         "mode":"casual",
         "completed":False
      },
      {
         "player":"alice",
         "duration_minutes":97,
         "score":1178,
         "mode":"ranked",
         "completed":True
      },
      {
         "player":"eve",
         "duration_minutes":18,
         "score":2661,
         "mode":"competitive",
         "completed":True
      },
      {
         "player":"bob",
         "duration_minutes":52,
         "score":761,
         "mode":"ranked",
         "completed":True
      },
      {
         "player":"eve",
         "duration_minutes":46,
         "score":2101,
         "mode":"casual",
         "completed":True
      },
      {
         "player":"charlie",
         "duration_minutes":117,
         "score":1359,
         "mode":"casual",
         "completed":True
      }
   ],
   "game_modes":[
      "casual",
      "competitive",
      "ranked"
   ],
   "achievements":[
      "first_blood",
      "level_master",
      "speed_runner",
      "treasure_seeker",
      "boss_hunter",
      "pixel_perfect",
      "combo_king",
      "explorer"
   ]
}

players = data_dictionary["players"]
sessions = data_dictionary["sessions"]

print("=== Game Analytics Dashboard ===\n")

print("=== List Comprehension Examples ===")
high_scorers = [p for p in players if players[p]["total_score"] > 2000]
double_score = [players[p]['total_score'] * 2 for p in players]
active_playters = [p for p in players if players[p]["sessions_played"] > 20]
print(f"High scorers (>2000): {high_scorers}")
print(f"Scores doubled: {double_score}")
print(f"Active players: {active_playters}\n")


print("=== Dict Comprehension Examples ===")
players_score = {p: players[p]["total_score"] for p in players}
print(f"Player scores: {players_score}")
scores = [
    data_dictionary["players"][player]["total_score"]
    for player in data_dictionary["players"]
]
score_categories = {
    "high": len([s for s in scores if s >= 2000]),
    "medium": len([s for s in scores if 1000 <= s < 2000]),
    "low": len([s for s in scores if s < 1000])
}
print(f"Score categories: {score_categories}")
achievement_count = {p: players[p]['achievements_count'] for p in players}
print(f"Achievement counts: {achievement_count}\n")

print("=== Set Comprehension Examples ===")
unique_players = {p['player'] for p in sessions}
print(F"Unique players: {unique_players}")
unique_achievements = {achievement for achievement in data_dictionary["achievements"]}
print(F"Unique achievements: {unique_achievements}")
active_regions = {p['mode'] for p in sessions}
print(F"Active regions: {active_regions}\n")

print("=== Combined Analysis ===")
count_players = len({p for p in players})
print(f"Total players: {count_players}")
total_unique_achievements = sum([players[p]['achievements_count'] for p in players])
print(f"Total unique achievements: {total_unique_achievements}")
average_score = sum(players_score[key] for key in players_score) / count_players
print(f"Average score: {average_score:.2f}")


def get_dict_value(k):
  return players_score[k]

top_performer = max(players_score, key=get_dict_value)
print(f"{top_performer} ({players_score[top_performer]} points, " 
      + f"{achievement_count[top_performer]} achievements)")
