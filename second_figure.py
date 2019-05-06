df2=pd.read_csv("/home/b/Downloads/inter.csv",converters={"Category":pd.to_datetime})

bot=90
top=130
fig, ax = plt.subplots(2,1)
ax[1].plot(df2['Category'][bot:top],(df2['SE-FLA megawatthours'][bot:top])/df2['SE-FLA megawatthours'].mean(),ls="steps")
ax[1].set_ylabel("Normalize Power Interchange")
ax[1].set_title("SE to FLA Exchange")
myFmt = DateFormatter("%m/%d:%H")
ax[1].xaxis.set_major_formatter(myFmt)
fig.autofmt_xdate()

ax[0].plot(df2['Category'][bot:top],(df2['SE-MIDW megawatthours'][bot:top])/df2['SE-MIDW megawatthours'].mean(),ls="steps")
ax[0].set_ylabel("Normalize Power Interchange")
ax[0].set_title("SE to MIDW Exchange")
myFmt = DateFormatter("%m/%d:%H")
ax[0].xaxis.set_major_formatter(myFmt)
fig.set_size_inches(10, 8)

