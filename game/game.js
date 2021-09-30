// import './js/libs/weapp-adapter'
// import './js/libs/symbol'

// import Main from './js/main'

// new Main()

const canvas = wx.createCanvas()

const context = canvas.getContext('2d') // 创建一个 2d context
context.fillStyle = '#1aad19' // 矩形颜色
const { windowWidth, windowHeight } = wx.getSystemInfoSync()
function drawRect(x, y) {
  context.clearRect(0, 0, windowWidth, windowHeight)
  context.fillRect(x, y, 100, 100)
}

drawRect(canvas.width / 2 - 50, 0)
const rectX = canvas.width / 2 - 50
let rectY = 0
setInterval(function(){
  drawRect(rectX, rectY++)
}, 16)
