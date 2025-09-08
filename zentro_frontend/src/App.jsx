// src/App.jsx
import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import MainLayout from "./components/layout/MainLayout"; // asume que usa Sidebar/Header
import DashboardPage from "./pages/DashboardPage";

// clientes
import ClientList from "./components/clientes/ClientList";
import ClientForm from "./components/clientes/ClientForm";

// recepción
import CheckIn from "./components/recepcion/CheckIn";
import GuestList from "./components/recepcion/GuestList";
import MembershipStatus from "./components/recepcion/MembershipStatus";

// membresias
import MembershipList from "./components/membresias/MembershipList";
import MembershipForm from "./components/membresias/MembershipForm";
import MembershipAssign from "./components/membresias/MembershipAssign";

// clases
import ClassCalendar from "./components/clases/ClassCalendar";
import ClassSchedule from "./components/clases/ClassSchedule";
import ClassBooking from "./components/clases/ClassBooking";
import ClassForm from "./components/clases/ClassForm";

// entrenadores
import TrainerList from "./components/entrenadores/TrainerList";
import TrainerProfile from "./components/entrenadores/TrainerProfile";
import TrainerForm from "./components/entrenadores/TrainerForm";

// rutinas
import RoutineList from "./components/rutinas/RoutineList";
import RoutineBuilder from "./components/rutinas/RoutineBuilder";
import ExerciseLibrary from "./components/rutinas/ExerciseLibrary";

// nutricion
import NutritionPlanList from "./components/nutricion/NutritionPlanList";
import DietForm from "./components/nutricion/DietForm";
import FoodDatabase from "./components/nutricion/FoodDatabase";

// tienda
import ProductList from "./components/tienda/ProductList";
import ProductForm from "./components/tienda/ProductForm";
import POS from "./components/tienda/POS";

// incidentes
import IncidentList from "./components/incidentes/IncidentList";
import IncidentForm from "./components/incidentes/IncidentForm";
import IncidentDetail from "./components/incidentes/IncidentDetail";

// administracion
import UserList from "./components/administracion/users/UserList";
import UserForm from "./components/administracion/users/UserForm";
import RoleManagement from "./components/administracion/roles/RoleManagement";
import PermissionList from "./components/administracion/permisos/PermissionList";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<MainLayout />}>
          <Route index element={<DashboardPage />} />

          <Route path="clientes" element={<ClientList />} />
          <Route path="clientes/nuevo" element={<ClientForm />} />
          <Route path="clientes/:id" element={<ClientForm />} />

          <Route path="recepcion/checkin" element={<CheckIn />} />
          <Route path="recepcion/guestlist" element={<GuestList />} />
          <Route path="recepcion/status" element={<MembershipStatus />} />

          <Route path="membresias" element={<MembershipList />} />
          <Route path="membresias/nuevo" element={<MembershipForm />} />
          <Route path="membresias/asignar" element={<MembershipAssign />} />

          <Route path="clases/calendar" element={<ClassCalendar />} />
          <Route path="clases/schedule" element={<ClassSchedule />} />
          <Route path="clases/book" element={<ClassBooking />} />
          <Route path="clases/nuevo" element={<ClassForm />} />

          <Route path="entrenadores" element={<TrainerList />} />
          <Route path="entrenadores/:id" element={<TrainerProfile />} />
          <Route path="entrenadores/nuevo" element={<TrainerForm />} />

          <Route path="rutinas" element={<RoutineList />} />
          <Route path="rutinas/builder" element={<RoutineBuilder />} />
          <Route path="rutinas/library" element={<ExerciseLibrary />} />

          <Route path="nutricion" element={<NutritionPlanList />} />
          <Route path="nutricion/diet" element={<DietForm />} />
          <Route path="nutricion/foods" element={<FoodDatabase />} />

          <Route path="tienda" element={<ProductList />} />
          <Route path="tienda/nuevo" element={<ProductForm />} />
          <Route path="tienda/pos" element={<POS />} />

          <Route path="incidentes" element={<IncidentList />} />
          <Route path="incidentes/nuevo" element={<IncidentForm />} />
          <Route path="incidentes/:id" element={<IncidentDetail />} />

          <Route path="admin/users" element={<UserList />} />
          <Route path="admin/users/nuevo" element={<UserForm />} />
          <Route path="admin/roles" element={<RoleManagement />} />
          <Route path="admin/permisos" element={<PermissionList />} />

          {/* fallback */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
