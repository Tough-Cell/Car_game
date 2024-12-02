def rank(score):
  rank = ""

  if score >= 0:
    rank = "Nooblet"
  if score >= 10:
    rank = "Noob"
  if score >= 50:
    rank = "Newbie"
  if score >= 70:
    rank = "Novice"
  if score >= 150:
    rank = "Neophyte"
  if score >= 200: 
    rank = "Dabbler"
  if score >= 250:
    rank = "Initiate"
  if score >= 300:
    rank = "Apprentice"
  if score >= 350:
    rank = "Pupil"
  if score >= 400:
    rank = "Learner"
  if score >= 450:
    rank = "Practitioner"
  if score >= 500:
    rank = "Semi-Pro"
  if score >= 600:
    rank = "Adept" 
  if score >= 700:
    rank = "Expert" 
  if score >= 800:
    rank = "Pro" 
  if score >= 900:
    rank = "Wizard" 
  if score >= 1000:
    rank = "Master" 
  if score >= 1100:
    rank = "Scholar" 
  if score >= 1200:
    rank = "Grandmaster" 
  if score >= 1300:
    rank = "Legend" 
  if score >= 1400:
    rank = "Chad" 
  if score >= 1500:
    rank = f"{int(score//1000)}Millionaire"


  return rank
