Attribute VB_Name = "Module1"
Sub StockMarketCal()

For Each WS In Worksheets
    WS.Activate
    Dim col As Integer
    col = 1
    Dim ticker As String
    Dim Volume As Double
    Volume = 0
    Dim Summary_Table_Row As Integer
    Summary_Table_Row = 2
    Dim openPrice As Double
    openPrice = Cells(2, 3).Value
    Dim closePrice As Double
    Dim yearlyChange As Double
    Dim percentChange As Double
    Range("I1").Value = "Ticker"
    Range("J1").Value = "Yearly Change"
    Range("K1").Value = "Percent Change"
    Range("L1").Value = "Total Stock Volume"
    
    lastRow = WS.Cells(Rows.Count, 1).End(xlUp).Row
    oneColRow = WS.Cells(Rows.Count, 10).End(xlUp).Row
    
        For i = 2 To lastRow
        
            If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
                ticker = Cells(i, 1).Value
                Range("I" & Summary_Table_Row).Value = ticker
                
                closePrice = Cells(i, 6).Value
                yearlyChange = closePrice - openPrice
                Range("J" & Summary_Table_Row).Value = yearlyChange
    
                    If (openPrice = 0 And closePrice = 0) Then
                        percentChange = 0
                    ElseIf (openPrice = 0 And closePrice <> 0) Then
                        percentChange = 1
                    Else
                        percentChange = yearlyChange / openPrice
                        Range("K" & Summary_Table_Row).Value = percentChange
                        Range("K" & Summary_Table_Row).NumberFormat = "00.0%"
                        
                    End If
    
                Volume = Volume + Cells(i, 7).Value
                Range("L" & Summary_Table_Row).Value = Volume
                            
                openPrice = Cells(i + 1, 3)
                Summary_Table_Row = Summary_Table_Row + 1
                Volume = 0
            Else
                Volume = Volume + Cells(i, 7).Value
            End If
            
        Next i
    
        For j = 2 To oneColRow
            If Cells(j, 10).Value > 0 Or Cells(j, 10).Value = 0 Then
                Cells(j, 10).Interior.ColorIndex = 4
            ElseIf Cells(j, 10).Value < 0 Then
                Cells(j, 10).Interior.ColorIndex = 3
            End If
        Next j
    
        Range("N2").Value = "Greatest % Increase"
        Range("N3").Value = "Greatest % Decrease"
        Range("N4").Value = "Greatest Total Volume"
        Range("O1").Value = "Ticker"
        Range("P1").Value = "Value"
    
        For W = 2 To oneColRow
            If Cells(W, 11).Value = Application.WorksheetFunction.Max(WS.Range("K2:K" & oneColRow)) Then
                Cells(2, 15).Value = Cells(W, 9).Value
                Cells(2, 16).Value = Cells(W, 11).Value
                Cells(2, 16).NumberFormat = "0.00%"
            ElseIf Cells(W, 11).Value = Application.WorksheetFunction.Min(WS.Range("K2:K" & oneColRow)) Then
                Cells(3, 15).Value = Cells(W, 9).Value
                Cells(3, 16).Value = Cells(W, 11).Value
                Cells(3, 16).NumberFormat = "0.00%"
            ElseIf Cells(W, 12).Value = Application.WorksheetFunction.Max(WS.Range("L2:L" & oneColRow)) Then
                Cells(4, 15).Value = Cells(W, 9).Value
                Cells(4, 16).Value = Cells(W, 12).Value
            End If
        Next W

Next WS

End Sub


