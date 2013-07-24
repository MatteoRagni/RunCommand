if (get_window_class()=="Runcommand") then
  -- Rendi semitrasparente la finestra selezionata
	os.execute("sleep 0.3 && transset-df -i " .. get_window_xid() .. " 0.7")
	-- os.execute("notify-send -t 0 " .. '"' .. "transset-df -i " .. get_window_xid() .. " 0.6" .. '"')
end
