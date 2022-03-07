const canvas = document.querySelector('canvas')
const container = document.getElementById('container')

console.log(canvas)
console.log(canvas.clientWidth, canvas.clientHeight)
console.log(container)

const clock = new THREE.Clock()
const scene = new THREE.Scene()
const textureLoader = new THREE.TextureLoader() 
// scene.background = new THREE.Color(0xa0a0a0)
// scene.fog = new THREE.Fog(0xa0a0a0, 10, 500)

const envSize = 256;
const cubeRenderTarget1 = new THREE.WebGLCubeRenderTarget( envSize )
const cubeCamera1 = new THREE.CubeCamera( 1, 1000, cubeRenderTarget1 )

const camera = new THREE.PerspectiveCamera(45, (container.clientWidth/2) / container.clientHeight, 0.01, 100)
camera.position.set(3, -1, 3)

const renderer = new THREE.WebGLRenderer({antialias: true, canvas: canvas, alpha: true})
renderer.setPixelRatio(window.devicePixelRatio)
renderer.setSize(container.clientWidth/2, container.clientHeight, false)
renderer.outputEncoding = THREE.sRGBEncoding
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap

const ambLight = new THREE.AmbientLight(0x404040)
scene.add(ambLight)

const hemiLight = new THREE.HemisphereLight( 0xffffff, 0x444444 );
hemiLight.position.set( 0, 100, 0 );
scene.add( hemiLight );

const dirLight = new THREE.DirectionalLight( 0xffffff );
dirLight.position.set( - 0, 40, 50 );
dirLight.castShadow = true;
dirLight.shadow.camera.top = 50;
dirLight.shadow.camera.bottom = - 25;
dirLight.shadow.camera.left = - 25;
dirLight.shadow.camera.right = 25;
dirLight.shadow.camera.near = 0.1;
dirLight.shadow.camera.far = 200;
dirLight.shadow.mapSize.set( 1024, 1024 );
scene.add( dirLight );

const boxGeometry = new THREE.BoxGeometry(1, 1, 1)
const boxMaterial = new THREE.MeshPhysicalMaterial({
    color: 0xddddff,
    metalness: 0.9,
    roughness: 0.0,
    reflectivity: 0.8, 
})

const cubeMesh = new THREE.Mesh(boxGeometry, boxMaterial)
camera.lookAt(cubeMesh.position)
cubeMesh.position.set(0, 1, 0)
scene.add(cubeMesh)

window.onresize = function () {
    camera.aspect = (container.clientWidth/2) / container.clientHeight
    camera.updateProjectionMatrix()
    renderer.setSize(container.clientWidth/2, container.clientHeight, false)
}

function animate() {
    const timer = 0.0001 * Date.now();
    requestAnimationFrame(animate)
    const delta = clock.getDelta()
    cubeMesh.rotation.y = timer * Math.PI
    cubeMesh.rotation.z = timer * Math.PI
    renderer.render(scene, camera)
}

animate()
