# INFO

## Параметры запроса
"
'graphid' => [T_ZBX_INT, O_MAND, P_SYS, DB_ID, null],
'from' => [T_ZBX_RANGE_TIME, O_OPT, P_SYS, null, null],
'to' => [T_ZBX_RANGE_TIME, O_OPT, P_SYS, null, null],
'profileIdx' => [T_ZBX_STR, O_OPT, null, null, null],
'profileIdx2' => [T_ZBX_STR, O_OPT, null, null, null],
'width' => [T_ZBX_INT, O_OPT, null, BETWEEN(CLineGraphDraw::GRAPH_WIDTH_MIN, 65535), null],
'height' => [T_ZBX_INT, O_OPT, null, BETWEEN(CLineGraphDraw::GRAPH_HEIGHT_MIN, 65535), null],
'outer' => [T_ZBX_INT, O_OPT, null, IN('0,1'), null],
'onlyHeight' => [T_ZBX_INT, O_OPT, null, IN('0,1'), null],
'legend' => [T_ZBX_INT, O_OPT, null, IN('0,1'), null],
'widget_view' => [T_ZBX_INT, O_OPT, null, IN('0,1'), null]
"
