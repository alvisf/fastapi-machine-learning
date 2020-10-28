from model import train, predict, convert
train()
prediction_list = predict()
convert(prediction_list)
train("GOOG")
train("AAPL")
train("^GSPC")