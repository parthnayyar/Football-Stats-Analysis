import pandas as pd
import matplotlib.pyplot as plt

isl_df = pd.read_csv('isl_data.csv')
print(isl_df.to_string())
print()

#get summary of imported dataframe
#variable.info()
isl_df.info()
print()

#finding sum, mean, std, min,... of a column
#variable[colname].sum()...
print('Total goals by all teams:', isl_df['scoresFor'].sum())
print('Most goals by a team:', isl_df['scoresFor'].max())
print('Min goals by a team:', isl_df['scoresFor'].min())
print()

#slicing is similar to lists
print(isl_df.loc[0])
print()

print(isl_df.loc[[0,3,5]].to_string())
print()

print(isl_df.loc[3:8].to_string())
print()

print(isl_df.iloc[-1])
print()

#display team with position 1
print(isl_df.loc[isl_df['position']==1])
print()

#displaying all teams who scored more than 25 goals
print(isl_df.loc[isl_df['scoresFor']>25].to_string())
print()

#displaying only name and goals scored of the teams who scored more than 25 goals
print(isl_df.loc[isl_df['scoresFor']>25,['team.name','scoresFor']].to_string())
print()

#adding more than one condition: displaying team name, goals scored, goals conceded of those teams that scored more than 25 and conceded less than 25
print(isl_df.loc[(isl_df['scoresFor']>25) & (isl_df['scoresAgainst']<=25),['team.name','scoresFor','scoresAgainst']].to_string())
print()
