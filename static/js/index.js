let load_data_pie1 = function (arg) {
    let init_pie1 = function (data_r) {
        let myChart1 = echarts.init(document.getElementById('pie1'));
        let option = {
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            // legend: {
            //     x: 'right',
            // },
            series: [
                {
                    name: '详细',
                    type: 'pie',
                    selectedMode: 'single',
                    radius: [0, '35%'],

                    label: {
                        normal: {
                            position: 'inner'
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                },
                {
                    label: {
                        formatter: "{b}:{d}%",
                    },
                    name: '详细',
                    type: 'pie',
                    radius: ['40%', '55%'],
                }
            ]
        };

        var data_obj = JSON.parse(data_r)
        let d1 = []
        let d2 = []
        for (let k in data_obj['outside']) {
            d1.push({value: data_obj['outside'][k], name: k.toString()})
        }
        for (let k in data_obj['inside']) {
            d2.push({value: data_obj['inside'][k], name: k.toString()})
        }
        option['series'][1]['data'] = d1
        option['series'][0]['data'] = d2
        myChart1.setOption(option, true);
    }
    let query_data = {
        query_date: arg
    }
    $.ajax({
        url: '/api/get_distinguish_list/',
        data: query_data,
        type: 'POST',
        success: function (data) {
            init_pie1(data)
        },
    })
}


let init_table1 = function () {
    let columns = [
        {title: '使用情况', field: 'flow_num'},
    ]
    $('#flow_table').bootstrapTable({
        method: 'POST',
        url: "/api/get_flow_list/",//请求路径
        pageList: [10],
        pagination: true,//是否分页
        sidePagination: 'client',//server:服务器端分页|client：前端分页
        search: true,
        pageSize: 10,//单页记录数
        showRefresh: true,//刷新按钮
        columns: [
            {
                title: '流程',
                field: 'flow',
                width: '220px',

            },
            {
                title: '使用情况',
                field: 'flow_num',
                sortable: true,
                formatter: operation2
            },
        ],
    });
}

function operation2(value, row, index) {
    var htm = '<div style="background-color: ' + choose_color(value) + '">' + value + '</div>'
    return htm
}

let reload_table1 = function (arg) {
    let query_data = {
        query_date: arg
    }
    $.ajax({
        url: '/api/get_flow_list/',
        type: 'POST',
        data: query_data,
        success: function (data) {
            var data_obj = JSON.parse(data)
            $('#flow_table').bootstrapTable('load', data_obj)
        },
    })
}

let load_OA_Histogram = function () {
    let init_OA_Histogram = function (data_r) {
        var myChart1 = echarts.init(document.getElementById('OA_Histogram'));
        let option = {
            legend: {},
            tooltip: {},
            dataset: {
                dimensions: [],
                source: []
            },
            xAxis: {type: 'category'},
            yAxis: {},
            // Declare several bar series, each will be mapped
            // to a column of dataset.source by default.
            series: [
                {
                    type: 'bar', label: {
                        normal: {
                            show: true
                        }
                    },
                },
                {
                    type: 'bar', label: {
                        normal: {
                            show: true
                        }
                    },
                },
                {
                    type: 'bar', label: {
                        normal: {
                            show: true
                        }
                    },
                },
                {
                    type: 'bar', label: {
                        normal: {
                            show: true
                        }
                    },
                },
                {
                    type: 'bar', label: {
                        normal: {
                            show: true
                        }
                    },
                },

            ]
        };
        let op_data = {}
        var data_obj = JSON.parse(data_r)
        data_obj.forEach(function (v, k) {
            if (!op_data[v['m']])
                op_data[v['m']] = {product: v['m'],}
            op_data[v['m']][v['company']] = v['num']
        })
        option['dataset']['dimensions'] = ["product", "UPG", "UPPG", "UPC", "UPZ", "集团公用"]
        option['dataset']['source'] = Object.values(op_data)
        myChart1.setOption(option);
    }
    $.ajax({
        url: '/api/get_oauser_list/',
        type: 'get',
        success: function (data) {
            init_OA_Histogram(data)
        }
    })
}


let choose_color = function (i) {
    if (i < 10) return '#fee7e1'
    if (i < 50) return '#fed1c3'
    if (i < 100) return '#fec2b0'
    if (i < 500) return '#fdb09b'
    if (i < 1000) return '#fd8f72'
    return '#fc5834'
}

let init_rseview_period = function () {
    for (let i = 1; i < 13; i++) {
        $('#rseview_period_table thead tr').append('<th>' + i + '</th>')
        $('#rseview_period_table tbody tr').append('<td>0</td>')
    }

    $.ajax({
        url: '/api/get_rseview_period_list/',
        type: 'get',
        success: function (data) {
            var data_obj = JSON.parse(data)
            let xuhao = {'下午': 1, '上午': 2, '晚上': 3, '深夜': 4, '凌晨': 5}
            data_obj.forEach(function (v, k) {
                for (let i in v) {
                    let hang = k + 1
                    $('#rseview_period_table tbody tr:nth-child(' + xuhao[i] + ') td:nth-child(' + hang + ')').text(v[i])
                    $('#rseview_period_table tbody tr:nth-child(' + xuhao[i] + ') td:nth-child(' + hang + ')').css('background-color', choose_color(v[i]))

                }

            })
        }
    })


}
let load_avg_table = function (arg) {

    let init_avg_table = function (data_r) {
        var myChart1 = echarts.init(document.getElementById('avg_table'));
        let option = {
            tooltip: {
                trigger: 'item',
                formatter: "{b}: {c}小时"
            },
            legend: {},
            xAxis: {
                type: 'category',
            },
            yAxis: {
                type: 'value'
            },
            series: [{
                name: '平均审批时长：（小时）',
                type: 'bar',
                itemStyle: {
                    color: '#aeb9c0'
                },
                label: {
                    normal: {
                        show: true
                    }
                },
            }]
        };

        var data_obj = JSON.parse(data_r)
        option['xAxis']['data'] = Object.keys(data_obj)
        option['series'][0]['data'] = Object.values(data_obj)
        console.log(Object.keys(data_obj))
        if (Object.keys(data_obj).length != 0)
            myChart1.setOption(option);
    }
    let query_data = {
        query_date: arg
    }

    $.ajax({
        url: '/api/get_avg_reply_time/',
        type: 'POST',
        data: query_data,
        success: function (data) {
            init_avg_table(data)
        }
    })
}

let load_lable_data = function (arg) {
    let query_data = {
        query_date: arg
    }
    $.ajax({
        url: '/api/get_lable_data/',
        type: 'POST',
        data: query_data,
        success: function (data) {
            var data_obj = JSON.parse(data)
            $('#label_data span:nth-child(1)').text('单数合计:' + data_obj['all'])
            $('#label_data span:nth-child(2)').text('退单数:' + data_obj['back'])
            $('#label_data span:nth-child(3)').text('超预算单:' + data_obj['beyond'])
        }
    })
}

window.onload = function () {
    $(function () {
        $('#collapseOne').collapse('show')
    });
    $(function () {
        $('#collapseTwo').collapse('show')
    });

    $('#selectDateTimePicker').datetimepicker({
        format: 'YYYY-MM',
        locale: moment.locale('zh-cn'),
    }).on('dp.change', function (e) {
        let datetime = $('#selectDateTimePicker input').val()
        load_data_pie1(datetime)
        reload_table1(datetime)
        load_avg_table(datetime)
        load_lable_data(datetime)
    })

    $('#selectDateTimePicker2').datetimepicker({
        format: 'YYYY',
        locale: moment.locale('zh-cn'),
    }).on('dp.change', function (e) {
        let datetime = $('#selectDateTimePicker2 input').val()
        load_data_pie1(datetime)
        reload_table1(datetime)
        load_avg_table(datetime)
        load_lable_data(datetime)
    }).hide()

    $('#sel_year').on("change", function () {
        var checkbox = $(this);
        if (checkbox[0].checked) {
            $('#selectDateTimePicker').hide()
            $('#selectDateTimePicker2').show()

        } else {
            $('#selectDateTimePicker').show()
            $('#selectDateTimePicker2').hide()

        }
    });

    load_data_pie1()
    init_table1()
    load_OA_Histogram()
    init_rseview_period()
    load_avg_table()
    load_lable_data()
}
