'use strict';
// Layout review adapters only; all card costs and fixture transitions use the base page.
const originalLayoutRender=render;
function pileMarkup(layers){return layers?Array.from({length:layers},(_,i)=>'<span class="pile-card" style="--pile-level:'+i+'" aria-hidden="true">'+backSkin()+'</span>').join(''):'<span class="pile-empty" aria-hidden="true">空</span>';}
function setHandOpen(open){$('hand-fan').hidden=!open;$('hand-pile').setAttribute('aria-expanded',String(open));$('hand-pile').setAttribute('aria-label',(open?'收起':'展开')+'手牌卡堆，'+state.hand.length+'张');document.querySelector('.hand-dock').classList.toggle('hand-open',open);}
render=function(){originalLayoutRender();$('bench-mode').textContent=state.future;$('bench-mode').disabled=!canEdit();$('hand-pile').innerHTML=pileMarkup(state.hand.length);setHandOpen(!$('hand-fan').hidden);};
$('resource-piles').innerHTML=['Ⅰ','Ⅱ','Ⅲ'].map(n=>'<div class="resource-pile card-pile" role="img" aria-label="资源卡堆'+n+'，造型占位">'+pileMarkup(4)+'<span class="pile-index" aria-hidden="true">'+n+'</span></div>').join('');
$('hand-pile').addEventListener('click',()=>setHandOpen($('hand-fan').hidden));
$('hand-fold').addEventListener('click',()=>{setHandOpen(false);$('hand-pile').focus();});
$('arrange').addEventListener('click',()=>setHandOpen(arranging));
$('scene').addEventListener('change',()=>setHandOpen(false));
$('reset').addEventListener('click',()=>setHandOpen(false));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!$('detail').open&&!$('hand-fan').hidden&&!layoutDrag?.active){setHandOpen(false);$('hand-pile').focus();}});
$('bench-mode').addEventListener('click',()=>{if(!canEdit())return;state.future=state.future==='普通积累'?'集中兑现':'普通积累';render();toast('下一批：'+state.future+' · 当前批次不变');});
$('layout-guides').addEventListener('change',e=>document.querySelector('.app').classList.toggle('show-layout-guides',e.target.checked));
let layoutDrag=null,suppressCardClickUntil=0;
function clearLayoutDrag(){if(!layoutDrag)return;layoutDrag.source.classList.remove('drag-origin');layoutDrag.ghost?.remove();layoutDrag.hint?.remove();document.querySelectorAll('.drop-valid').forEach(el=>el.classList.remove('drop-valid'));document.body.classList.remove('is-dragging');layoutDrag=null;}
function layoutDropTarget(x,y){
 const hit=document.elementFromPoint(x,y),card=hit?.closest('.card[data-zone]');
 if(card){const zone=card.dataset.zone,index=Number(card.dataset.index);if(zone==='enemy'||(zone===layoutDrag.zone&&index===layoutDrag.index)||(zone==='hand'&&layoutDrag.zone==='hand'))return null;return{zone,index,id:state[zone][index]?.id,element:card.parentElement};}
 const empty=hit?.closest('#player-cards .empty-card');
 if(empty&&layoutDrag.zone==='hand'&&state.table.length<5){const index=[...$('player-cards').children].indexOf(empty.parentElement);if(index===state.table.length)return{empty:true,element:empty.parentElement};}
 return null;
}
document.addEventListener('pointerdown',e=>{
 const source=e.target.closest('.card[data-zone]');if(e.button!==0||!source||source.dataset.zone==='enemy'||!canEdit()||playing||$('detail').open)return;
 const rect=source.getBoundingClientRect(),zone=source.dataset.zone,index=Number(source.dataset.index);
 layoutDrag={source,zone,index,id:state[zone][index].id,x:e.clientX,y:e.clientY,offsetX:e.clientX-rect.left,offsetY:e.clientY-rect.top,width:rect.width,height:rect.height,active:false,pointerId:e.pointerId};
});
document.addEventListener('pointermove',e=>{
 if(!layoutDrag||e.pointerId!==layoutDrag.pointerId)return;
 if(!layoutDrag.active){if(Math.hypot(e.clientX-layoutDrag.x,e.clientY-layoutDrag.y)<7)return;layoutDrag.active=true;layoutDrag.source.classList.add('drag-origin');layoutDrag.ghost=layoutDrag.source.cloneNode(true);for(const name of [...layoutDrag.ghost.attributes].map(a=>a.name))if(name.startsWith('data-'))layoutDrag.ghost.removeAttribute(name);layoutDrag.ghost.classList.add('drag-card');layoutDrag.ghost.tabIndex=-1;layoutDrag.ghost.setAttribute('aria-hidden','true');Object.assign(layoutDrag.ghost.style,{width:layoutDrag.width+'px',height:layoutDrag.height+'px'});document.body.append(layoutDrag.ghost);layoutDrag.hint=document.createElement('div');layoutDrag.hint.className='drag-hint';document.body.append(layoutDrag.hint);document.body.classList.add('is-dragging');}
 e.preventDefault();Object.assign(layoutDrag.ghost.style,{left:e.clientX-layoutDrag.offsetX+'px',top:e.clientY-layoutDrag.offsetY+'px'});
 document.querySelectorAll('.drop-valid').forEach(el=>el.classList.remove('drop-valid'));const target=layoutDropTarget(e.clientX,e.clientY);layoutDrag.target=target;
 if(target&&state.ap>0)target.element.classList.add('drop-valid');layoutDrag.hint.textContent=state.ap<=0?'整理点不足':target?(target.empty?'补入最左空位 · 1点':'交换位置 · 1点'):'拖至桌牌或手牌 · Esc取消';
 Object.assign(layoutDrag.hint.style,{left:Math.min(e.clientX+15,window.innerWidth-210)+'px',top:Math.min(e.clientY+20,window.innerHeight-40)+'px'});
},{passive:false});
document.addEventListener('pointerup',e=>{
 if(!layoutDrag||e.pointerId!==layoutDrag.pointerId)return;if(!layoutDrag.active){clearLayoutDrag();return;}
 const drag=layoutDrag,target=layoutDropTarget(e.clientX,e.clientY);suppressCardClickUntil=performance.now()+350;clearLayoutDrag();
 if(!canEdit()||playing||state[drag.zone][drag.index]?.id!==drag.id)return;
 if(!target)return toast('已放回原位');if(state.ap<=0)return toast('整理点不足，牌位保持不变');
 if(!target.empty&&state[target.zone][target.index]?.id!==target.id)return;
 picks=[{zone:drag.zone,index:drag.index}];if(!target.empty)picks.push({zone:target.zone,index:target.index});
 applyArrangement();document.querySelector('[data-focus="'+(target.empty?'table-'+(state.table.length-1):target.zone+'-'+target.index)+'"]')?.focus();
});
document.addEventListener('click',e=>{if(performance.now()<suppressCardClickUntil&&e.target.closest('.card[data-zone]')){e.preventDefault();e.stopImmediatePropagation();}},true);
document.addEventListener('pointercancel',clearLayoutDrag);
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&layoutDrag?.active){e.preventDefault();suppressCardClickUntil=performance.now()+350;clearLayoutDrag();toast('已取消拖动');}},true);
window.addEventListener('blur',clearLayoutDrag);
document.addEventListener('dragstart',e=>{if(e.target.closest('.card'))e.preventDefault();});
render();
