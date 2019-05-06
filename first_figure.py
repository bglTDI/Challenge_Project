df=pd.read_csv("/home/b/Downloads/demand_and_forecast.csv",converters={"Category":pd.to_datetime})

fig, ax = plt.subplots(2,2)

ax[0,0].plot(df["Category"],df["CAL demand megawatthours"],color='tab:blue',drawstyle="steps")
ax[0,0].plot(df["Category"],df["CAL demand forecast megawatthours"],color='tab:blue',ls="--",drawstyle="steps")
ax[0,0].plot(df["Category"],df["NYIS demand megawatthours"],color="tab:orange",drawstyle="steps")
ax[0,0].plot(df["Category"],df["NYIS demand forecast megawatthours"],color="tab:orange",ls="--",drawstyle="steps")
ax[0,0].xaxis.set_major_formatter(myFmt)
ax[0,0].set_ylim([10000,42000])
myFmt = DateFormatter("%m/%d")
fig.autofmt_xdate()
ax[0,0].set_ylabel("Power Demand (mWh)")
ax[0,0].legend(("CAL Actual","CAL Forecasted","NYIS Actual","NYIS Forecated"),loc="upper right")

ax[0,1].plot(df["Category"],df["SE demand megawatthours"],color='tab:red',drawstyle="steps")
ax[0,1].plot(df["Category"],df["SE demand forecast megawatthours"],"--",color='tab:red',ls="--",drawstyle="steps")
ax[0,1].plot(df["Category"],df["SW demand megawatthours"],color='tab:green',drawstyle="steps")
ax[0,1].plot(df["Category"],df["SW demand forecast megawatthours"],"--",color='tab:green',ls="--",drawstyle="steps")
ax[0,1].set_ylim([0,70000])
ax[0,1].xaxis.set_major_formatter(myFmt)
ax[0,1].set_ylabel("Power Demand (mWh)")
ax[0,1].legend(("SE Actual","SE Forecasted","SW Actual","SW Forecated"),loc="upper right")


ax[1,0].plot(df["Category"],(df["CAL demand megawatthours"]-df["CAL demand forecast megawatthours"])/df["CAL demand megawatthours"],color='tab:blue',ls="steps")
ax[1,0].plot(df["Category"],(df["NYIS demand megawatthours"]-df["NYIS demand forecast megawatthours"])/df["NYIS demand megawatthours"],color='tab:orange',ls="steps")
ax[1,0].xaxis.set_major_formatter(myFmt)
ax[1,0].set_ylabel("Relative Forecast Error")
ax[1,0].legend(("CAL Error","NYIS Error"),loc="upper right")


ax[1,1].plot(df["Category"],(df["SE demand megawatthours"]-df["SE demand forecast megawatthours"])/df["SE demand megawatthours"],color='tab:red',ls="steps")
ax[1,1].plot(df["Category"],(df["SW demand megawatthours"]-df["SW demand forecast megawatthours"])/df["SW demand megawatthours"],color='tab:green',ls="steps")
ax[1,1].set_ylim([-1,1])
ax[1,1].xaxis.set_major_formatter(myFmt)
ax[1,1].set_ylabel("Relative Forecast Error")
ax[1,1].legend(("SE Error","SW Error"),loc="upper right")

fig.set_size_inches(20, 16.5)
